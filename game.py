import RPi.GPIO as GPIO 
import time
import sys
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

index = 1



def apply():
    buzzer.play(0.001)
    match index:
        case 1:
            leds.turn_off_all()
            leds.tehran.on()
        case 2:
            leds.turn_off_all()
            leds.providence.on()           
        case 3:
            leds.turn_off_all()
            leds.reject.on()           
        case 4:
            leds.turn_off_all()
            leds.error.on()
                 


apply()

while True: # Run forever

    # white button
    try:
        # red button
        if GPIO.input(pin_red) == GPIO.LOW and red_pressed == False:
            red_pressed = True
            index+=1
            if index>4: index = 4

            apply()
            wait_for_next()

        if GPIO.input(pin_red) == GPIO.HIGH:
            red_pressed = False

        # green button
        if GPIO.input(pin_green) == GPIO.LOW and green_pressed == False:
            print("@ Green Button is pressed")
            green_pressed = True
            index-=1
            if index<0: index = 1

            apply()
            wait_for_next()

        if GPIO.input(pin_green) == GPIO.HIGH:
            green_pressed = False

        
        



    except KeyboardInterrupt:
        print('\r\nbye bye!')
        break



