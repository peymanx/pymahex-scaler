#!/usr/bin/env python
# -*- coding: utf-8 -*-
import serial

port = "/dev/ttyS0"
bytes_sent = 12
serialPort = serial.Serial(port, 9600, timeout = 1)

while True:
    print("...")
    
    loopback = serialPort.read(bytes_sent)
    print(loopback)
    print(loopback.decode('utf-8'))

