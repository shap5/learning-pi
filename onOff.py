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

x=1    
while (x==1): #infinite loop
    response=easygui.buttonbox(msg='Turn the light',title='Light Switch',choices=('On','Off','Quit'))
    if response=='On':
	GPIO.output(led,1)
    elif response=='Off':
	GPIO.output(led,0)
    elif response=='Quit':
	break

#cleanup and end
GPIO.cleanup()
