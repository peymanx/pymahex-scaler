import serial, os
from pyfiglet import Figlet

f = Figlet(font='slant')


port = "/dev/ttyS0"
bytes_sent = 24
serialPort = serial.Serial(port, 9600, timeout = 0.1)
buffer = ''

print(str(float('00.0'))+ "             ",end='\r')
def normalize(s):
    return s.replace(" ", "").replace("\r", "").replace("\n", "")
last = -1.0
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
                #print(str(float(weight))+ "kg             \033[?25l",end='\r')
                fweight = float(weight)
                if last != fweight:
                    os.system('clear')
                    print(f.renderText( str(fweight)))
                    last = fweight
            except:
                ...
    except KeyboardInterrupt:
        print('\033[?25h', end="")
        print('\r\nbye bye!')
        break
