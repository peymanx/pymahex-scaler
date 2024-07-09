import RPi.GPIO as gpio
import time
import sys

print('Leds Tester')

pin_tehran = 24
pin_others = 25
pin_reject = 8
pin_error = 7

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
    match sys.argv[1]:
        case 'tehran':
              if sys.argv[2] == 'on':
                turn_on(pin_tehran)
              else:
                turn_off(pin_tehran)
        case 'other' | 'others' | 'ostan' | 'shahrestan' | 'providence':
             if sys.argv[2] == 'on':
                turn_on(pin_others)
             else:
                turn_off(pin_others)
        case 'reject' | 'rj' | 'mazad':
             if sys.argv[2] == 'on':
                turn_on(pin_reject)
             else:
                turn_off(pin_reject)
        case 'error' | 'err': 
             if sys.argv[2] == 'on':
                turn_on(pin_error)
             else:
                turn_off(pin_error)
        case 'all': 
             if sys.argv[2] == 'on':
                turn_on(pin_tehran)
                turn_on(pin_others)
                turn_on(pin_reject)
                turn_on(pin_error)
             else:
                 turn_off(pin_tehran)
                 turn_off(pin_others)
                 turn_off(pin_reject)
                 turn_off(pin_error)
