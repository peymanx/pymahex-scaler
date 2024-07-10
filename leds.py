import RPi.GPIO as gpio
import time
import sys

print('Leds Tester')

tehran = 18
providence = 22
reject = 24
error = 26

gpio.setmode(gpio.BOARD)
gpio.setwarnings(False)
gpio.setup(tehran, gpio.OUT)
gpio.setup(providence, gpio.OUT)
gpio.setup(reject, gpio.OUT)
gpio.setup(error, gpio.OUT)

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
                turn_on(tehran)
              else:
                turn_off(tehran)
        case 'other' | 'others' | 'ostan' | 'shahrestan' | 'providence':
             if sys.argv[2] == 'on':
                turn_on(providence)
             else:
                turn_off(providence)
        case 'reject' | 'rj' | 'mazad':
             if sys.argv[2] == 'on':
                turn_on(reject)
             else:
                turn_off(reject)
        case 'error' | 'err': 
             if sys.argv[2] == 'on':
                turn_on(error)
             else:
                turn_off(error)
        case 'all': 
             if sys.argv[2] == 'on':
                turn_on(tehran)
                turn_on(providence)
                turn_on(reject)
                turn_on(error)
             else:
                 turn_off(tehran)
                 turn_off(providence)
                 turn_off(reject)
                 turn_off(error)
