import threading
import push_buttons, buzzer


def background_service():
    push_buttons.listen()


service = threading.Thread(name='background', target=background_service)
service.daemon = True
service.start()

while True:
       try:
           barcode = input('Scan the parcel\'s barcode: ')
           print('The barcode is: ' + barcode)

           if barcode in ["-1", "exit","q"]:
                break
           if barcode == 'buzz':
                buzzer.play()

       except KeyboardInterrupt:
           break
            
buzzer.silent()        
print('bye bye')