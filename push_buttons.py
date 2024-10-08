import RPi.GPIO as GPIO 
import time
from color import *
import buzzer, leds

pin_white = 40
pin_red = 12
pin_green = 16

GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD)

GPIO.setup(pin_white, GPIO.IN)
GPIO.setup(pin_red, GPIO.IN)
GPIO.setup(pin_green, GPIO.IN)

white_pressed = False
green_pressed = False
red_pressed = False

leds.turn_off_all()

def wait_for_next():
    time.sleep(0.4)

def listen():
    while True: 
        try:
            if GPIO.input(pin_white) == GPIO.LOW and white_pressed == False:
                print("@ White button is pressed", color=print.HIGHLIGHTED)
                white_pressed = True
                leds.tehran.invert()
                buzzer.play(0.001)
                wait_for_next()
                
            if GPIO.input(pin_white) == GPIO.HIGH:
                white_pressed = False

            # red button
            if GPIO.input(pin_red) == GPIO.LOW and red_pressed == False:
                print("@ Red Button is pressed", color=print.HIGHLIGHTED_RED)
                red_pressed = True
                leds.error.invert()
                buzzer.play(2)
                wait_for_next()

            if GPIO.input(pin_red) == GPIO.HIGH:
                red_pressed = False

            # green button
            if GPIO.input(pin_green) == GPIO.LOW and green_pressed == False:
                print("@ Green Button is pressed", color=print.HIGHLIGHTED_GREEN_LIGHT)
                green_pressed = True
                leds.tehran.invert()
                buzzer.play(0.001)
                leds.providence.invert()
                leds.reject.invert()
                wait_for_next()

            if GPIO.input(pin_green) == GPIO.HIGH:
                green_pressed = False
        except KeyboardInterrupt:
            print('\r\nbye bye!')
            break



