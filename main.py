import threading
import push_buttons


def service():
    push_buttons.wait_for_a_key()



push_button_service = threading.Thread(name='background', target=service)
push_button_service.daemon = True
push_button_service.start()

while True:
    barcode = input('Scan the parcel barcode: ')
    print('The barcode is: ' + barcode)
    pass