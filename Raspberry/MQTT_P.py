import paho.mqtt.client as mqtt

broker_addr="broker's ip address"
mqttc = mqtt.Client("Pub")
mqttc.connect(broker_addr)
mqttc.publish("hello/world","hello")
mqttc.publish("world","world")

