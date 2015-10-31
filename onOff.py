import RPi.GPIO as GPIO
import time

led=21
right_button=13
left_button=19

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(led,GPIO.OUT)
GPIO.setup(right_button, GPIO.IN, GPIO.PUD_UP)
GPIO.setup(left_button, GPIO.IN, GPIO.PUD_UP)

for x in range(0,3):	
    GPIO.output(led,1)
    time.sleep(1)
    GPIO.output(led,0)
    time.sleep(1)

GPIO.cleanup()
