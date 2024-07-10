import leds, time


leds.turn_off_all()

index = 1

while True:
    match index:
        case 1:
            leds.tehran.on()
        case 2:
            leds.providence.on()           
        case 3:

            leds.reject.on()           
        case 4:
            leds.error.on()         
        case 5:  
            leds.turn_off_all()
        case 6:  
            leds.turn_on_all()
        case 7:  
            index=0
    index+=1       
    time.sleep(0.4)



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
    time.sleep(0.4)




