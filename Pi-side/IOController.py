import RPi.GPIO as GPIO


LED_PIN = 4 

class IOController:

    def __init__(self,led_pin=LED_PIN):
        self.ledpin = led_pin
        GPIO.setmode(GPIO.BCM) 
        GPIO.setup(self.ledpin,GPIO.OUT)

    def setLed(self, state):
        GPIO.output(LED_PIN, state)