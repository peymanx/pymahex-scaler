from myserial import Serial
import time

ras_ser = Serial('/dev/ttyS0', 9600, timeout= 1)
ras_ser.flush()
while True:
    line = ras_ser.readline().decode('utf-8').rstrip()
    print(line)
    time.sleep(1)

