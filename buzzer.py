import RPi.GPIO as gpio
import time, sys

pin = 37

gpio.setmode(gpio.BOARD)
gpio.setup(pin, gpio.OUT)


def play(delay=0.5):
    gpio.output(pin, gpio.HIGH)
    time.sleep(delay)
    silent()

def silent():
    gpio.output(pin, gpio.LOW)


if __name__ == '__main__':
    delay = 0.5
    global Buzz 
    Buzz = gpio.PWM(pin, 440) 
    Buzz.start(50) 
    if len(sys.argv)>1:
            delay = float(sys.argv[1])
    play(delay)
    silent()