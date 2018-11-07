import paho.mqtt.client as mqtt
import time

def on_message(client, userdata, message):
	print(str(message.payload))

broker='localhost'
client = mqtt.Client("Test")
client.on_message = on_message
client.connect(broker)
client.subscribe("hello/world")
time.sleep(4)
client.loop_forever()
