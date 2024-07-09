import RPi.GPIO as gpio
import time
import sys

print('Leds Tester')

pin_tehran = 7
pin_others = 8
pin_reject = 25
pin_error = 24

gpio.setmode(gpio.BCM)
gpio.setwarnings(False)
gpio.setup(pin_tehran, gpio.OUT)
gpio.setup(pin_others, gpio.OUT)
gpio.setup(pin_reject, gpio.OUT)
gpio.setup(pin_error, gpio.OUT)

def turn_on(pin):
     gpio.output(pin, gpio.HIGH)
     print("Turning on " + str(pin))

def turn_off(pin):
     gpio.output(pin, gpio.LOW)
     print("Turning off " + str(pin))

if len(sys.argv)>1:
    print(sys.argv[0])
    print(sys.argv[1])
    match sys.argv[0]:
        case 'tehran':
              if sys.argv[1] == 'on':
                turn_on(pin_tehran)
              else:
                turn_off(pin_tehran)
        case 'other':
             if sys.argv[1] == 'on':
                turn_on(pin_others)
             else:
                turn_off(pin_others)
        case 'reject':
             if sys.argv[1] == 'on':
                turn_on(pin_reject)
             else:
                turn_off(pin_reject)
        case 'error': 
             if sys.argv[1] == 'on':
                turn_on(pin_error)
             else:
                turn_off(pin_error)
