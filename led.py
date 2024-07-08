import RPi.GPIO as gpio
import time

pin = 7

gpio.setmode(gpio.BCM)
gpio.setup(pin, gpio.OUT)

while True:
        gpio.output(pin, gpio.HIGH)
        print('on')
        time.sleep(1)
        gpio.output(pin, gpio.LOW)
        print('off')
        time.sleep(1)