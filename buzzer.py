import RPi.GPIO as gpio
import time

pin = 26

gpio.setmode(gpio.BCM)
gpio.setup(pin, gpio.OUT)

# Buzzer
gpio.output(pin, gpio.HIGH)
print('Buzzer beeeeeeeeeeeez')
time.sleep(5)
gpio.output(pin, gpio.LOW)
print('Buzzer off')
