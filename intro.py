import leds, time


leds.turn_off_all()

index = 1

while True:
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
    index+=1
    if index > 4: index=1
    time.sleep(1/index)




