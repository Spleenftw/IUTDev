#!/usr/bin/env python3

import paho.mqtt.client as mqtt
import time
from gpiozero import MCP3004

while True:
    time.sleep(2)
    def on_connect(client, userdata, flags, rc):
        print("Connected with result code "+str(rc))
        client.subscribe("sensors")


    def on_message(client, userdata, msg):
        mqtttest=msg.payload.decode()
        print(mqtttest)

    username="b19sr"
    password="samantharaphael"
    client = mqtt.Client()
    client.username_pw_set(username, password)
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect("194.199.227.235", 1148)

    divider = MCP3004(0)
    x=divider.value*100
    #str = open('data.txt', 'r').read()
    client.publish("home/test/test", x)


