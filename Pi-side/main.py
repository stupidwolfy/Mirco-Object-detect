# Import packages
import os
import argparse
import cv2
import numpy as np
import sys
import time
import importlib.util
import threading

import socket
import imagezmq
from halo import Halo
import zmq
from func_timeout import func_timeout, FunctionTimedOut


from IOController import IOController
from VideoStream import VideoStream
from Setting import Setting
from MqttController import MqttController
from WebRequestController import WebRequest

#load setting file
S_LED_PIN, S_MODEL_NAME, S_GRAPH_NAME, S_LABELMAP_NAME, S_min_conf_threshold, S_imW, S_imH, S_obj_trigger, S_need_detect_all, S_server_url, S_mqtt_broker, S_mqtt_port, S_mqtt_topic, S_webRequest = Setting.loadSetting()

# Define and parse input arguments
parser = argparse.ArgumentParser()
#parser.add_argument('--modeldir', help='Folder the .tflite file is located in',
#                    required=True)
#parser.add_argument('--graph', help='Name of the .tflite file, if different than detect.tflite',
#                    default='detect.tflite')
#parser.add_argument('--labels', help='Name of the labelmap file, if different than labelmap.txt',
#                    default='labelmap.txt')
#parser.add_argument('--threshold', help='Minimum confidence threshold for displaying detected objects',
#                    default=0.5)
#parser.add_argument('--resolution', help='Desired webcam resolution in WxH. If the webcam does not support the resolution entered, errors may occur.',
#                    default='800x600')
#parser.add_argument('--edgetpu', help='Use Coral Edge TPU Accelerator to speed up detection',
#                    action='store_true')
#parser.add_argument('--trigger', help='Object to active action.',
#                    default='cell phone,person')

parser.add_argument('--modeldir', help='Folder the .tflite file is located in',
                    default=S_MODEL_NAME)
parser.add_argument('--graph', help='Name of the .tflite file, if different than detect.tflite',
                    default=S_GRAPH_NAME)
parser.add_argument('--labels', help='Name of the labelmap file, if different than labelmap.txt',
                    default=S_LABELMAP_NAME)
parser.add_argument('--threshold', help='Minimum confidence threshold for displaying detected objects',
                    default=S_min_conf_threshold)
parser.add_argument('--resolution', help='Desired webcam resolution in WxH. If the webcam does not support the resolution entered, errors may occur.',
                    default=str(S_imW)+"x"+str(S_imH))
parser.add_argument('--edgetpu', help='Use Coral Edge TPU Accelerator to speed up detection',
                    action='store_true')
parser.add_argument('--trigger', help='Object to active action.',
                    default=S_obj_trigger)

args = parser.parse_args()

MODEL_NAME = args.modeldir
GRAPH_NAME = args.graph
LABELMAP_NAME = args.labels
min_conf_threshold = float(args.threshold)
resW, resH = args.resolution.split('x')
imW, imH = int(resW), int(resH)
use_TPU = args.edgetpu

server_url = S_server_url

# Import TensorFlow libraries
# If tflite_runtime is installed, import interpreter from tflite_runtime, else import from regular tensorflow
# If using Coral Edge TPU, import the load_delegate library
pkg = importlib.util.find_spec('tflite_runtime')
if pkg:
    from tflite_runtime.interpreter import Interpreter
    if use_TPU:
        from tflite_runtime.interpreter import load_delegate
else:
    from tensorflow.lite.python.interpreter import Interpreter
    if use_TPU:
        from tensorflow.lite.python.interpreter import load_delegate

# If using Edge TPU, assign filename for Edge TPU model
if use_TPU:
    # If user has specified the name of the .tflite file, use that name, otherwise use default 'edgetpu.tflite'
    if (GRAPH_NAME == 'detect.tflite'):
        GRAPH_NAME = 'edgetpu.tflite'       

# Get path to current working directory
CWD_PATH = os.getcwd()

# Path to .tflite file, which contains the model that is used for object detection
PATH_TO_CKPT = os.path.join(CWD_PATH,MODEL_NAME,GRAPH_NAME)

# Path to label map file
PATH_TO_LABELS = os.path.join(CWD_PATH,MODEL_NAME,LABELMAP_NAME)

# Load the label map
with open(PATH_TO_LABELS, 'r') as f:
    labels = [line.strip() for line in f.readlines()]

# Have to do a weird fix for label map if using the COCO "starter model" from
# https://www.tensorflow.org/lite/models/object_detection/overview
# First label is '???', which has to be removed.
if labels[0] == '???':
    del(labels[0])

# Load the Tensorflow Lite model.
# If using Edge TPU, use special load_delegate argument
if use_TPU:
    interpreter = Interpreter(model_path=PATH_TO_CKPT,
                              experimental_delegates=[load_delegate('libedgetpu.so.1.0')])
    print(PATH_TO_CKPT)
else:
    interpreter = Interpreter(model_path=PATH_TO_CKPT)

interpreter.allocate_tensors()

# Get model details
input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()
height = input_details[0]['shape'][1]
width = input_details[0]['shape'][2]

floating_model = (input_details[0]['dtype'] == np.float32)

input_mean = 127.5
input_std = 127.5

#Thread variable
keep_runing = True
G_frame = None
G_newimg = False

Timer1 = {"Time": 10, "isCooldown": False}

# custom variable
dot_count = 1
#obj_find_atmp = 5 #attem to keep led on if obj go away
obj_trigger = args.trigger.split(',')
need_detect_all = S_need_detect_all #Trigger when found all obj or just one

spinner = Halo(text='Running', spinner='dots')

# Initialize frame rate calculation
frame_rate_calc = 1
freq = cv2.getTickFrequency()

# Initialize video stream
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (imW,imH))
videostream = VideoStream(resolution=(imW,imH),framerate=30).start()
time.sleep(1)

# Initialize video output
sender = imagezmq.ImageSender(connect_to=server_url)
rpi_name = socket.gethostname() # send RPi hostname with each image

# Initialize GPIO
ioController = IOController()
# Init Mqtt client
mqttController = MqttController(S_mqtt_broker, S_mqtt_port, S_mqtt_topic)
# Init Web Request
webRequest = WebRequest(S_webRequest)


def trigger_handle(obj_box, frame):
    global Timer1
    if obj_box:
        print("  Found| ", list(map(lambda x : labels[x] ,obj_box)))
        intersect_obj = set(obj_trigger).intersection(set(map(lambda x : labels[x] ,obj_box)))

        if(need_detect_all):
            if(all(item in list(map(lambda x : labels[x] ,obj_box)) for item in obj_trigger)):
                print("action Trigged. (all)"+ ",".join(obj_trigger))
                ioController.setLed(False)

                if not Timer1["isCooldown"]:
                    mqttController.sendMessage("Detected all ["+",".join(obj_trigger)+ "]")
                    data = {"content" : "Detected all ["+",".join(obj_trigger)+ "]"}
                    imencoded = cv2.imencode(".jpg", frame)[1]
                    webRequest.sendPost(data, imencoded)
                    Timer1["isCooldown"] = True
        else:
            if(any(item in list(map(lambda x : labels[x] ,obj_box)) for item in obj_trigger)):
                print("action Trigged. (any)")
                ioController.setLed(False)

                if not Timer1["isCooldown"]:
                    mqttController.sendMessage("Detected Some ["+",".join(intersect_obj)+"]")
                    data = {"content" : "Detected Some ["+",".join(intersect_obj)+"]"}
                    imencoded = cv2.imencode(".jpg", frame)[1]
                    webRequest.sendPost(data, imencoded)
                    Timer1["isCooldown"] = True

def imzmq_loop():
    global G_newimg
    while keep_runing:
        try:
            if G_newimg :
                sender.send_image(rpi_name, G_frame)
                G_newimg = False
            time.sleep(1)
        except zmq.error.ContextTerminated:
            continue


def timer_loop():
    global Timer1
    while keep_runing:
        if Timer1["isCooldown"]:
            time.sleep(Timer1["Time"])
            Timer1["isCooldown"] = False  #timer is cooled down, ready

zmqThread = threading.Thread(target=imzmq_loop, daemon=True)
timerThread = threading.Thread(target=timer_loop, daemon=True)

print("Init finished.")
#print("Status: starting record", end="\r", flush=True)
#for frame1 in camera.capture_continuous(rawCapture, format="bgr",use_video_port=True):

ioController.setLed(True)
timerThread.start()
zmqThread.start()
spinner.start()
while True:
    obj_found_box = []
    #print("Status: recoding frame [",dot_count ,"]", end="\r", flush=True)
    try:
        # Start timer (for calculating frame rate)
        t1 = cv2.getTickCount()
    
        # Grab frame from video stream
        frame1 = videostream.read()
        frame1= cv2.rotate(frame1, cv2.ROTATE_180)
    
        # Acquire frame and resize to expected shape [1xHxWx3]
        frame = frame1.copy()
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frame_resized = cv2.resize(frame_rgb, (width, height))
        input_data = np.expand_dims(frame_resized, axis=0)
    
        # Normalize pixel values if using a floating model (i.e. if model is non-quantized)
        if floating_model:
            input_data = (np.float32(input_data) - input_mean) / input_std
    
        # Perform the actual detection by running the model with the image as input
        interpreter.set_tensor(input_details[0]['index'],input_data)
        interpreter.invoke()
    
        # Retrieve detection results
        boxes = interpreter.get_tensor(output_details[0]['index'])[0] # Bounding box coordinates of detected objects
        classes = interpreter.get_tensor(output_details[1]['index'])[0] # Class index of detected objects
        scores = interpreter.get_tensor(output_details[2]['index'])[0] # Confidence of detected objects
        #num = interpreter.get_tensor(output_details[3]['index'])[0]  # Total number of detected objects (inaccurate and not needed)
    
        # Loop over all detections and draw detection box if confidence is above minimum threshold
        for i in range(len(scores)):
            if ((scores[i] > min_conf_threshold) and (scores[i] <= 1.0)):
                # Get bounding box coordinates and draw box
                # Interpreter can return coordinates that are outside of image dimensions, need to force them to be within image using max() and min()
                ymin = int(max(1,(boxes[i][0] * imH)))
                xmin = int(max(1,(boxes[i][1] * imW)))
                ymax = int(min(imH,(boxes[i][2] * imH)))
                xmax = int(min(imW,(boxes[i][3] * imW)))
                
                cv2.rectangle(frame, (xmin,ymin), (xmax,ymax), (10, 255, 0), 2)
    
                # Draw label
                object_name = labels[int(classes[i])] # Look up object name from "labels" array using class index
                label = '%s: %d%%' % (object_name, int(scores[i]*100)) # Example: 'person: 72%'
                labelSize, baseLine = cv2.getTextSize(label, cv2.FONT_HERSHEY_SIMPLEX, 0.7, 2) # Get font size
                label_ymin = max(ymin, labelSize[1] + 10) # Make sure not to draw label too close to top of window
                cv2.rectangle(frame, (xmin, label_ymin-labelSize[1]-10), (xmin+labelSize[0], label_ymin+baseLine-10), (255, 255, 255), cv2.FILLED) # Draw white box to put label text in
                cv2.putText(frame, label, (xmin, label_ymin-7), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 0), 2) # Draw label text
                #print("Found %s" %(object_name))
                obj_found_box.append(int(classes[i]))

        # Draw framerate in corner of frame
        cv2.putText(frame,'FPS: {0:.2f}'.format(frame_rate_calc),(30,50),cv2.FONT_HERSHEY_SIMPLEX,1,(255,255,0),2,cv2.LINE_AA)
        
        trigger_handle(obj_found_box, frame)
        # All the results have been drawn on the frame, so it's time to display it.
        #cv2.imshow('Object detector', frame)
        #out.write(frame)
        
        #sender.send_image(rpi_name, frame)
        #New Image is ready
        G_frame = frame
        G_newimg = True
    
        # Calculate framerate
        t2 = cv2.getTickCount()
        time1 = (t2-t1)/freq
        frame_rate_calc= 1/time1

        dot_count +=1
        # Press 'q' to quit
        if cv2.waitKey(1) == ord('q'):
            break

    except KeyboardInterrupt:
        spinner.stop()
        print("Status: exiting", end="\r", flush=True)
        ioController.cleanIO()
        break

print("Status: Cleaning up, please wait...", end="\r", flush=True)
# Clean up
keep_runing =False
out.release()
videostream.stop()
#sender.close()
timerThread.join()
zmqThread.join(5)
cv2.destroyAllWindows()
print("                                              ", end="\r", flush=True)
print("Status: finished")
print()
