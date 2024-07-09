#!/usr/bin/env python
# -*- coding: utf-8 -*-
import serial, time
test_string = "hello 123kg".encode('utf-8')
port= "/dev/ttyS0"

while True:
    serialPort = serial.Serial(port, 9600, timeout = 2)
    print ("Serial port", port, " ready for test :")
    bytes_sent = serialPort.write(test_string)
    print ("Sended", bytes_sent, "byte")
    time.sleep(0.5)

