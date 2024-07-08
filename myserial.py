import serial

def connect(port):
    return serial.Serial(port, baudrate=9600, timeout=1)

ser = connect('/dev/ttyS0')
buf = bytearray()
while True:

    num_bytes = max(1, min(1024, ser.in_waiting))
    data = ser.read(num_bytes)
    if data:
        buf.extend(data)
        print(data)
    else:
        # no data to read aka disconnection has occurred
        ser = connect('/dev/ttyS0')
        if ser.isOpen():
            continue
        else:
            # could not reconnect
            break