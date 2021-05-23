import paho.mqtt.client as mqtt

class MqttController:
    def __init__(self, broker, port, topic):
        self.client = mqtt.Client()
        self.client.connect(broker, port=port)
        self.topic = topic

    def sendMessage(self, msg):
        self.client.publish(self.topic, msg)
