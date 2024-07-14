import serial, os
from pyfiglet import Figlet


global display_on_screen, last
display_on_screen = False
last = -1.0


def normalize(s):
    return s.replace(" ", "").replace("\r", "").replace("\n", "")

def get():
    return last

def listen():    
    global display_on_screen, last
    port = "/dev/ttyS0"
    bytes_sent = 24
    serialPort = serial.Serial(port, 9600, timeout = 0.01)
    buffer = ''     
    f = Figlet(font='smblock')  
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
                        if display_on_screen:
                            print('\033[5A\033[2K', end='')
                            f = Figlet(font='smblock')                        
                            fig= f"{fweight:2.2f}kg"
                            print(f.renderText(fig))
                        last = fweight
                except:
                    ...

                    
        except KeyboardInterrupt:
            if display_on_screen:
                print('\033[?25h', end="")
                print('\r\nbye bye!')
            break

if __name__ == '__main__':
    os.system('clear')
    display_on_screen = True
    listen()
