import RPi.GPIO as gpio
import time
import sys



print('Led Tester')

pin = 7

if len(sys.argv)>1:
        pin = sys.argv[1]


print('Tesing pin %d' % pin)

gpio.setmode(gpio.BCM)
gpio.setup(pin, gpio.OUT)

while True:
        gpio.output(pin, gpio.HIGH)
        print('on')
        time.sleep(1)
        gpio.output(pin, gpio.LOW)
        print('off')
        time.sleep(1)