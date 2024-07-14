import threading
import push_buttons


def background_service():
    push_buttons.listen()


service = threading.Thread(name='background', target=background_service)
service.daemon = True
service.start()

while True:
       try:
           barcode = input('Scan the parcel barcode: ')
           print('The barcode is: ' + barcode)

           if barcode in ["-1", "exit","q"]:
                break
       except KeyboardInterrupt:
           break
            

        