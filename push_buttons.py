import RPi.GPIO as GPIO 
import time
import sys

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

while True: # Run forever

    # white button
    if GPIO.input(pin_white) == GPIO.LOW and white_pressed == False:
        print("@ Button White is pressed")
        white_pressed = True
        time.sleep(0.5)
    if GPIO.input(pin_white) == GPIO.HIGH:
        white_pressed = False

    # red button
    if GPIO.input(pin_red) == GPIO.LOW and red_pressed == False:
        print("@ Button Red is pressed")
        red_pressed = True
        time.sleep(0.5)
    if GPIO.input(pin_red) == GPIO.HIGH:
        red_pressed = False

    # green button
    if GPIO.input(pin_green) == GPIO.LOW and green_pressed == False:
        print("@ Button Green is pressed")
        green_pressed = True
        time.sleep(0.5)
    if GPIO.input(pin_green) == GPIO.HIGH:
        green_pressed = False


