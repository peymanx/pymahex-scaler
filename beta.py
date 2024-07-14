
import threading, time

global money
money = 0

def background():
    global money
    while True:
        number = int(input('Enter:'))
        money += number
        print('Money:', money)

def foreground():
    global money
    while True:
        money+=1
        time.sleep(1)


b = threading.Thread(name='background', target=background)
b.daemon = True
f = threading.Thread(name='foreground', target=foreground)
f.daemon = True

b.start()
f.start()

while True:
    ...