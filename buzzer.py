import RPi.GPIO as gpio
import sys
from time import sleep

pin = 37

gpio.setwarnings(False)
gpio.setmode(gpio.BOARD)
gpio.setup(pin, gpio.OUT)


def play(delay=0.1):
    gpio.output(pin, gpio.HIGH)
    sleep(delay)
    silent()

def silent():
    gpio.output(pin, gpio.LOW)

def click():
    play(0.003)
    sleep(0.01)
    play(0.002)

def intro():
    play(0.1)
    sleep(0.5)

    play(0.01)
    sleep(0.01)
    play(0.01)
    sleep(0.5)

    play(0.01)
    sleep(0.01)
    play(0.01)
    sleep(0.5)

    sleep(1)
    play(0.5)


def error():
    play(0.9)

if __name__ == '__main__':
    delay = 0.5
    global Buzz 
    Buzz = gpio.PWM(pin, 440) 
    start(50) 
    if len(sys.argv)>1:
            delay = float(sys.argv[1])
    play(delay)
    silent()