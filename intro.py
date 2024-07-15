import leds, time, buzzer

leds.turn_off_all()

def run(n=12):
    index = 1
    while n>0:
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
        buzzer.play(0.003)
        if index > 4: index=1
        time.sleep(0.6)
        n-=1


if __name__ == '__main__':
    run()
    

