import serial

def connect(port):
    return serial.Serial(port, baudrate=9600, timeout=1)

ser = connect('/dev/ttyS0')
buf = bytearray()
print('here')
while True:
    num_bytes = max(100, min(1024, ser.in_waiting))
    print(num_bytes.decode("utf-8"))
    data = ser.read(num_bytes)
    print('data: ' + str(data))
    if data:
        buf.extend(data)
    else:
        ser = connect('/dev/ttyS0')
        if ser.isOpen():
            continue
        else:
            print('failto connect')
            break






