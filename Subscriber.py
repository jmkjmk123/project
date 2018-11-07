import paho.mqtt.client as mqtt
import os
import time

def on_message(client, userdata, msg):
	topic=msg.topic
	if topic is "Exit":
		if str(msg.payload) is "off":
			print("time out" + '\n')
			client.loop_stop()
		else :
			pass
	print (msg.topic + " : " + str(msg.payload))

broker_addr="localhost"
client = mqtt.Client()
client.on_message = on_message
client.connect(broker_addr)
client.subscribe("CLK")
client.subscribe("TMP")
client.subscribe("CDS")
client.loop_forever()
