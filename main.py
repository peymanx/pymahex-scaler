import threading
import push_buttons, buzzer
import api as Api
import leds, weight


def push_buttons_service():
    push_buttons.listen()

def weight_service():
    weight.listen()

pushbtn_service = threading.Thread(name='push_buttons_service', target=push_buttons_service)
pushbtn_service.daemon = True
pushbtn_service.start()

w_service = threading.Thread(name='push_buttons_service', target=weight_service)
w_service.daemon = True
w_service.start()

while True:
       try:
           barcode = input('Scan the parcel\'s barcode: ')
           print('The barcode is: ' + barcode)
           w = weight.get()
           print(f'The weight is: {w}kg')

           
           if len(barcode)>3:
                result = Api.send_to_ecourier(barcode, 1)
                leds.turn_off_all()
                match result:
                    case Api.ApiResult.TEHRAN:
                        leds.tehran.on()       
                                 
                    case Api.ApiResult.PROVIDENCE:
                        leds.providence.on()    
                                    
                    case Api.ApiResult.REJECT:
                        leds.reject.on()
                        
                    case Api.ApiResult.ERROR:
                        leds.error.on()
                        buzzer.error()
           buzzer.click()
            
           if barcode in ["-1", "exit","q"]:
                break

       except KeyboardInterrupt:
           break
            
buzzer.silent() 
leds.turn_on_all()       
print('bye bye')