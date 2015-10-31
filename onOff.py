#imports
import RPi.GPIO as GPIO 
import time 
import easygui

#define pins
led=21

#initialize IO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

#setup pins
GPIO.setup(led,GPIO.OUT)
GPIO.output(led,0)
#############End Setup##############

msg = "Enter the timing for the LED"
title="Blinking LED"
fieldNames=["On1","Off1","On2","Off2","On3","Off3"]
fieldValues=[]
fieldValues=easygui.multenterbox(msg,title,fieldNames)

#cleanup and end
GPIO.cleanup()
