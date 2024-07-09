import RPi.GPIO as gpio
import time
import sys



print('Led Tester')
gpio.setwarnings(False)
pin = 7

if len(sys.argv)>1:
        pin = int(sys.argv[1])


print('Tesing pin %d' % pin)

gpio.setmode(gpio.BCM)
gpio.setup(pin, gpio.OUT)

while True:
        try:
            gpio.output(pin, gpio.HIGH)
            print('on')
            time.sleep(1)
            gpio.output(pin, gpio.LOW)
            print('off')
            time.sleep(1)
        except KeyboardInterrupt:
                print('Interrupted by user')
                break