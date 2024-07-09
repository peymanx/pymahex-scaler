import serial

def connect(port):
    return serial.Serial(port, baudrate=9600, timeout=1)

ser = connect('/dev/ttyS0')
buf = bytearray()
print('here')
while True:
    #print('.')
    num_bytes = 1
    num_bytes = max(100, min(1024, ser.in_waiting))
    print(num_bytes)
    data = ser.read(num_bytes)
    print('data: ' + str(data))
    if data:
        buf.extend(data)
    else:
        # no data to read aka disconnection has occurred
        #print('else')
        ser = connect('/dev/ttyS0')
        if ser.isOpen():
            #print('open')
            continue
        else:
            # could not reconnect
            print('failto connect')
            break






