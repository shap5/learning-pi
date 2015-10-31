import RPi.GPIO as GPIO
import time
import easygui

led=21
right_button=13
left_button=19

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(led,GPIO.OUT)
GPIO.setup(right_button, GPIO.IN, GPIO.PUD_UP)
GPIO.setup(left_button, GPIO.IN, GPIO.PUD_UP)

def response=(easygui.buttonbox(msg='Turn light on?',title='Light Switch',choices=["On","Off","Cancel"],image=None)
	
	if response==0:
		GPIO.output(led,1)
	elif response==1:
		GPIO.output(led,0)
	else
		break

GPIO.cleanup()
