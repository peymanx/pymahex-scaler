import RPi.GPIO as gpio
import sys



gpio.setmode(gpio.BOARD)
gpio.setwarnings(False)

class LED:
    def __init__(self, pin, name):
        self.pin = pin
        self.status = False
        self.name = name
        gpio.setup(pin, gpio.OUT)
    def on(self):
        gpio.output(self.pin, gpio.HIGH)
        #print(f"Turning LED named {self.name}({self.pin}): on" )
        self.status = True
    def off(self):
        gpio.output(self.pin, gpio.LOW)
        #print(f"Turning LED named {self.name}({self.pin}): off" )
        self.status = False
    def invert(self):
        if self.status == True:
            self.off()
        else:
            self.on()



tehran = LED(pin=18,name="Tehran")
providence = LED(22,name="Shahrestan Non-tehran")
reject = LED(24,"Mazad")
error = LED(26,"System Error")


leds = [ tehran, providence, reject, error]

def turn_on_all():
    for led in leds:
        led.on()


def turn_off_all():
    for led in leds:
        led.off()

if __name__ == '__main__':
    print('Leds Tester')
    if len(sys.argv)>1:
        match sys.argv[1]:
            case 'tehran':
                if sys.argv[2] == 'on':
                    tehran.on()
                else:
                    tehran.off()
            case 'other' | 'others' | 'ostan' | 'shahrestan' | 'providence':
                if sys.argv[2] == 'on':
                    providence.on()
                else:
                    providence.off()
            case 'reject' | 'rj' | 'mazad':
                if sys.argv[2] == 'on':
                    reject.on();
                else:
                    reject.off()
            case 'error' | 'err': 
                if sys.argv[2] == 'on':
                    error.on()
                else:
                    error.off()
            case 'all': 
                if sys.argv[2] == 'on':
                    turn_on_all()
                else:
                    turn_off_all()



