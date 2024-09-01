import serial, os



global  current_weight

last =-1.0
current_weight = 0.0


def normalize(s):
    return s.replace(" ", "").replace("\r", "").replace("\n", "")

def get():
    return current_weight

def listen():    
    global  current_weight, last
    port = "/dev/ttyS0"
    bytes_sent = 24
    serialPort = serial.Serial(port, 9600, timeout = 0.01)
    buffer = ''     
  
    while True:
        try:
            data = serialPort.read(bytes_sent)
            buffer+=data.decode()
            if len(buffer)>0:
                print(buffer)
                buffer = ''
        except:
            ...


listen()