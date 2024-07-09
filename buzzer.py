import RPi.GPIO as gpio
import time

pin = 26

gpio.setmode(gpio.BCM)
gpio.setup(pin, gpio.OUT)

# Buzzer
def play():
    gpio.output(pin, gpio.HIGH)
    print('Buzzer beeeeeeeeeeeez')
    time.sleep(0.5)
    gpio.output(pin, gpio.LOW)
    print('Buzzer off')


play()