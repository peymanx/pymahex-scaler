import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library

GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
GPIO.setup(21, GPIO.IN) # Set pin 10 to be an input pin and set initial value to be pulled low (off)
GPIO.setup(18, GPIO.IN) # Set pin 10 to be an input pin and set initial value to be pulled low (off)
GPIO.setup(23, GPIO.IN) # Set pin 10 to be an input pin and set initial value to be pulled low (off)


while True: # Run forever
    if GPIO.input(21) == GPIO.HIGH:
        print("Button 21 was pushed!")
    if GPIO.input(21) == GPIO.LOW:
        print("Button 21 was RELEASSED!")
    if GPIO.input(18) == GPIO.HIGH:
        print("Button 18 was pushed!")
    if GPIO.input(18) == GPIO.LOW:
        print("Button 18 was RELEASSED!")
    if GPIO.input(23) == GPIO.HIGH:
        print("Button 23 was pushed!")
    if GPIO.input(23) == GPIO.LOW:
        print("Button 23 was RELEASSED!")


PIO.input(18) == GPIO.HIGH:
print("Button 18 was pushed!")
PIO.input(23) == GPIO.HIGH:
print("Button 23 was pushed!")
