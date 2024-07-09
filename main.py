import buzzer, sys


delay = 0.5

if len(sys.argv)>1:
        delay = float(sys.argv[1])



buzzer.play(delay)