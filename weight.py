import serial, os
from pyfiglet import Figlet


global display_on_screen, current_weight
display_on_screen = False
last =-1.0
current_weight = 0.0


def normalize(s):
    return s.replace(" ", "").replace("\r", "").replace("\n", "")

def get():
    return current_weight

def listen():    
    global display_on_screen, current_weight, last
    port = "/dev/ttyS0"
    bytes_sent = 24
    serialPort = serial.Serial(port, 9600, timeout = 0.01)
    buffer = ''     
    f = Figlet()  
    tener = 0
    while True:
        try:
            tener+=1
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
                    if current_weight != fweight:
                        current_weight = fweight
                except:
                    ...
                    
            # if tener > 10:
            #     if len(buffer)==0: 
            #         last=0.0
            #     tener=0
                
            if display_on_screen and current_weight!= last:
                print('\033[5A\033[2K', end='')
                f = Figlet(font='smblock')                        
                fig= f"{current_weight:2.2f}kg        "
                print(f.renderText(fig))
                last = current_weight

                    
        except KeyboardInterrupt:
            if display_on_screen:
                print('\033[?25h', end="")
                print('\r\nbye bye!')
            break

if __name__ == '__main__':
    os.system('clear')
    display_on_screen = True
    listen()
