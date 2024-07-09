import serial

def connect(port):
    return serial.Serial(port, baudrate=9600, timeout=1)

my_serial = connect('/dev/ttyS0')
buf = bytearray()
print('here')
while True:
    num_bytes = max(1, min(1024, my_serial.in_waiting))
    data = my_serial.read(num_bytes)
    print(f'data: "{data.decode("utf-8")}"')
    if data:
        buf.extend(data)
    else:
        my_serial = connect('/dev/ttyS0')
        if my_serial.isOpen():
            continue
        else:
            print('failed to connect')
            break






