import RPi.GPIO as gpio
import time, sys

pin = 37

gpio.setmode(gpio.BOARD)
gpio.setup(pin, gpio.OUT)


p = gpio.PWM(12, 100)

c4 = 261
d4 = 294
e4 = 329
f4 = 349
g4 = 392
a4 = 440
b4 = 493
c5 = 523.25

speed = 0.1

gpio.output(12, True) 
p.start(10) # 10% duty cycle sounds 'ok'

p.ChangeFrequency(c4)
time.sleep(speed)
p.ChangeFrequency(d4)  
time.sleep(speed)
p.ChangeFrequency(e4)   
time.sleep(speed)
p.ChangeFrequency(f4)  
time.sleep(speed)
p.ChangeFrequency(g4)    
time.sleep(speed)
p.ChangeFrequency(a4)    
time.sleep(speed)
p.ChangeFrequency(b4)    
time.sleep(speed)
p.ChangeFrequency(c5)    
time.sleep(speed)

p.stop()
gpio.cleanup()