#!/usr/bin/env python
# -*- coding: utf-8 -*-
import serial

port = "/dev/ttyS0"
bytes_sent = 12

while True:
    print("...")
    try:
        serialPort = serial.Serial(port, 9600, timeout = 2)
        loopback = serialPort.read(bytes_sent)
        print(loopback)
        print(loopback.encode('utf-8'))

    except IOError:
        print ("Error on", port,"\n")