#!/usr/bin/env python
# -*- coding: utf-8 -*-
import serial

port = "/dev/ttyS0"
bytes_sent = 12
serialPort = serial.Serial(port, 9600, timeout = 1)
buffer = ''

while True:
    data = serialPort.read(bytes_sent)
    buffer+=data.decode()

    print(f'"{buffer}"\r\n****************************************************************')

