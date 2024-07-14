#!/home/luca/pi-rfid/env python

import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)
GPIO.setup(37, GPIO.OUT)
try:
	while True:
		print("Beep ON")
		GPIO.output(37, GPIO.LOW)
		sleep(0.3)
		GPIO.output(37, GPIO.HIGH)
		print("Beep OFF")
		sleep(5)
		
finally:
	GPIO.cleanup()