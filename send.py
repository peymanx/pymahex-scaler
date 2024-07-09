import serial



def connect(port):
    return serial.Serial(port, baudrate=9600, timeout=0.5)

my_serial = connect('/dev/ttyS0')


num_bytes = 1

while True:
    data = my_serial.read(num_bytes)
    print(data)






