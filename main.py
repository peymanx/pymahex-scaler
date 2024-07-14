import threading
import push_buttons, buzzer
import api as Api
import leds

def background_service():
    push_buttons.listen()


service = threading.Thread(name='background', target=background_service)
service.daemon = True
service.start()

while True:
       try:
           barcode = input('Scan the parcel\'s barcode: ')
           print('The barcode is: ' + barcode)
           buzzer.click();
           
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
                        
           if barcode in ["-1", "exit","q"]:
                break

       except KeyboardInterrupt:
           break
            
buzzer.silent() 
leds.turn_on_all()       
print('bye bye')