import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
import time
import sys

pin = 40

if len(sys.argv)>1:
        pin = int(sys.argv[1])


print('Tesing pin %d' % pin)

GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD)
GPIO.setup(pin, GPIO.IN) # Set pin 10 to be an input pin and set initial value to be pulled low (off)

white_pressed = False

while True: # Run forever
    if GPIO.input(pin) == GPIO.LOW and white_pressed == False:
        print("Button WHITE was pushed!")
        white_pressed = True
        time.sleep(0.5)



    if GPIO.input(pin) == GPIO.HIGH:
        white_pressed = False


