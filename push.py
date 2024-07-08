import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library


pin = 40
GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD)
GPIO.setup(pin, GPIO.IN) # Set pin 10 to be an input pin and set initial value to be pulled low (off)


while True: # Run forever
    if GPIO.input(pin) == GPIO.LOW:
        print("Button WHITE was pushed!")


