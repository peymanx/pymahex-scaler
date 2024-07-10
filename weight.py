import serial
import cursor
cursor.hide()

port = "/dev/ttyS0"
bytes_sent = 24
serialPort = serial.Serial(port, 9600, timeout = 0.1)
buffer = ''
print('Connecting to Scaler...')
print(str(float('00.0'))+ "             ",end='\r')
def normalize(s):
    return s.replace(" ", "").replace("\r", "").replace("\n", "")

while True:
    try:
        data = serialPort.read(bytes_sent)
        buffer+=data.decode()
        wn = buffer.rfind('wn') 
        kg = buffer.rfind('kg')
        dot = buffer.rfind('.')
        if wn != -1 and  kg != -1 and dot != -1:
            weight = normalize(buffer[wn+2:kg])
            buffer=''
            try:
                print(str(float(weight))+ "             ",end='\r')
            except:
                ...
    except KeyboardInterrupt:
        print('\r\nbye bye!')
        break
