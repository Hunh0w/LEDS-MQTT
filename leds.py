#!/usr/bin/env python3
#-- coding: utf-8 --

import RPi.GPIO as GPIO
from time import sleep
import paho.mqtt.client as mqtt

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
LED7 = 7
GPIO.setup(LED7, GPIO.OUT)
    
def led_handle():
    GPIO.output(LED7, GPIO.HIGH)
    sleep(0.05)
    GPIO.output(LED7, GPIO.LOW)
    sleep(0.05)
    
def on_connect(client, userdata, flags, rc):
    if rc != 0:
       print("result code : "+str(rc))
    print("Connected successfully")
    client.subscribe("avion")

def on_message(client, userdata, msg):
    led_handle()

client = mqtt.Client()
client.username_pw_set("adsb", password="XXXXXXXXX")
client.connect("194.199.227.235", 1136, 60)

client.on_connect = on_connect
client.on_message = on_message

client.loop_forever()
