#!/usr/bin/env python
# -*- coding: utf-8 -*-
import serial

port = "/dev/ttyS0"
bytes_sent = 24
serialPort = serial.Serial(port, 9600, timeout = 1)
buffer = ''

def normalize(s):
    return s.replace(" ", "").replace("\r", "").replace("\n", "")

while True:
    data = serialPort.read(bytes_sent)
    buffer+=data.decode()
    wn = buffer.rfind('wn') 
    kg = buffer.rfind('kg')
    dot = buffer.rfind('.')
    if wn != -1 and  kg != -1 and dot != -1:
        weight = normalize(buffer[wn+2:kg])
        try:
            print(float(weight))
        except:
            ...
        
        buffer=''

