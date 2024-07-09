import RPi.GPIO as gpio
import time

pin = 26

gpio.setmode(gpio.BCM)
gpio.setup(pin, gpio.OUT)

# Buzzer
def play(delay=0.5):
    gpio.output(pin, gpio.HIGH)
    print('Buzzer beeeeeeeeeeeez')
    time.sleep(delay)
    silent()

def silent():
    gpio.output(pin, gpio.LOW)
    print('Buzzer off')


if __name__ == '__main__':
    play()
    silent()