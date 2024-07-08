import time
import serial




ser = serial.serial(
        port='/dev/ttyAM0', #Replace ttyS0 with ttyAM0 for Pi1,Pi2,Pi0
        baudrate = 9600,

        timeout=1
)
counter=0

while True:
   line = ser.readline()
   if len(line) > 0:
      print(line);