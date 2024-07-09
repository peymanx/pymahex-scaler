#!/usr/bin/env python
# -*- coding: utf-8 -*-
import serial

port = "/dev/ttyS0"
bytes_sent = 24
serialPort = serial.Serial(port, 9600, timeout = 1)
buffer = ''

while True:
    data = serialPort.read(bytes_sent)
    buffer+=data.decode()
    wn = buffer.find('wn') 
    kg = buffer.find('kg')
    if wn != -1 and  kg != -1:
        weight = buffer[wn:kg]
        print(weight)
        buffer=''

