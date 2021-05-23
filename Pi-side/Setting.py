import pickle
import os

CMD_PATH = os.path.dirname(os.path.abspath(__file__))

#default setting, in case not found setting file
S_LED_PIN = 4
S_MODEL_NAME = "./models/Sample_TFLite_model"
S_GRAPH_NAME = "detect.tflite"
S_LABELMAP_NAME = "labelmap.txt"
S_min_conf_threshold = 0.5
S_imW = 800
S_imH = 600
S_obj_trigger = "vase, bottle"
S_need_detect_all = False
S_server_url = "tcp://192.168.1.26:5555"
S_mqtt_broker = "broker.mqttdashboard.com"
S_mqtt_port = 1883
S_mqtt_topic = "micro/iot1"

class Setting:
    @staticmethod
    def loadSetting():
        try:
            LED_PIN, MODEL_NAME, GRAPH_NAME, LABELMAP_NAME, min_conf_threshold, imW, imH, obj_trigger, need_detect_all, server_url, mqtt_broker, mqtt_port, mqtt_topic = pickle.load(open(os.path.join(CMD_PATH,"setting.pickle"), "rb"))
            return LED_PIN, MODEL_NAME, GRAPH_NAME, LABELMAP_NAME, min_conf_threshold, imW, imH, obj_trigger, need_detect_all, server_url, mqtt_broker, mqtt_port, mqtt_topic
        except (OSError, IOError) as e:
            return Setting.saveSetting()

    @staticmethod
    def saveSetting():
        data = [S_LED_PIN, S_MODEL_NAME, S_GRAPH_NAME, S_LABELMAP_NAME, S_min_conf_threshold, S_imW, S_imH, S_obj_trigger, S_need_detect_all, S_server_url, S_mqtt_broker, S_mqtt_port, S_mqtt_topic]
        pickle.dump(data, open(os.path.join(CMD_PATH,"setting.pickle"), "wb"))
        return S_LED_PIN, S_MODEL_NAME, S_GRAPH_NAME, S_LABELMAP_NAME, S_min_conf_threshold, S_imW, S_imH, S_obj_trigger, S_need_detect_all, S_server_url, S_mqtt_broker, S_mqtt_port, S_mqtt_topic

#if run directly, act as setting input
if __name__ == "__main__":
    S_LED_PIN, S_MODEL_NAME, S_GRAPH_NAME, S_LABELMAP_NAME, S_min_conf_threshold, S_imW, S_imH, S_obj_trigger, S_need_detect_all, S_server_url, S_mqtt_broker, S_mqtt_port, S_mqtt_topic = Setting.loadSetting()
    try:
        print("============= Setting ============")

        #Led pin
        print("Led pin (%s):" %S_LED_PIN, end="\r")
        while True:
            try:
                temp =input("\t\t")
                S_LED_PIN = int(temp) if temp else S_LED_PIN
                break
            except ValueError:
                print("Led pin (%s):              (Numer only!!!)" %S_LED_PIN, end="\r")
        
        #Model path
        print("Model path (%s):" %S_MODEL_NAME, end="\r")
        temp = input("\t\t\t\t\t\t")
        S_MODEL_NAME = temp if temp else S_MODEL_NAME

        #Tflite File
        print("tflite File(%s):" %S_GRAPH_NAME, end="\r")
        temp = input("\t\t\t\t")
        S_GRAPH_NAME = temp if temp else S_GRAPH_NAME
        
        #Label File
        print("label File( %s ):" %S_LABELMAP_NAME, end="\r")
        temp = input("\t\t\t\t")
        S_LABELMAP_NAME = temp if temp else S_LABELMAP_NAME

        #Min confidence
        print("Min confidence (%s):" %S_min_conf_threshold, end="\r")
        while True:
            try:
                temp =input("\t\t\t")
                S_min_conf_threshold = float(temp) if temp else S_min_conf_threshold
                break
            except ValueError:
                print("Min confidence ( %s ):              (Numer only!!!)" %S_min_conf_threshold, end="\r")

        #Image Width
        print("Image Width (%s):" %S_imW, end="\r")
        while True:
            try:
                temp =input("\t\t\t")
                S_imW = int(temp) if temp else S_imW
                break
            except ValueError:
                print("Min confidence ( %s ):              (Numer only!!!)" %S_imW, end="\r")

        #Image Height
        print("Image Height (%s):" %S_imH, end="\r")
        while True:
            try:
                temp =input("\t\t\t")
                S_imH = int(temp) if temp else S_imH
                break
            except ValueError:
                print("Image Height (%s):              (Numer only!!!)" %S_imH, end="\r")

        #Object target
        print("Object target a,..(%s)\n\t\t  :" %S_obj_trigger, end="\r")
        temp = input("\t\t\t")
        S_obj_trigger = temp if temp else S_obj_trigger

        #Server URL
        print("Server url(%s)\n\t\t  :" %S_server_url, end="\r")
        temp = input("\t\t\t")
        S_server_url = temp if temp else S_server_url

        #Detect all
        print("Detect all? y/n(%s):" %S_need_detect_all, end="\r")
        temp =input("\t\t\t")
        if temp:
            if temp.lower() == "y":
                 S_need_detect_all = True
            elif temp.lower() == "n":
                 S_need_detect_all = False

        #Mqtt broker
        print("Mqtt broker(%s)\n\t\t  :" %S_mqtt_broker, end="\r")
        temp = input("\t\t\t")
        S_mqtt_broker = temp if temp else S_mqtt_broker

        #Mqtt port
        print("Mqtt port (%s):" %S_mqtt_port, end="\r")
        while True:
            try:
                temp =input("\t\t\t")
                S_mqtt_port = int(temp) if temp else S_mqtt_port
                break
            except ValueError:
                print("Mqtt port (%s):              (Numer only!!!)" %S_mqtt_port, end="\r")

        #Mqtt topic
        print("Mqtt topic(%s)\n\t\t  :" %S_mqtt_topic, end="\r")
        temp = input("\t\t\t")
        S_mqtt_topic = temp if temp else S_mqtt_topic

        Setting.saveSetting()
        print()
        print("============= Finished ===========")

    except KeyboardInterrupt:
        print()
        print("============= Cenceled ===========")