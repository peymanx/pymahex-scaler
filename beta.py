
from pathlib import Path

def log(barcode, weight):

    bar = Path(__file__).with_name('barcode.txt')
    with open(bar, "w") as file:
        file.write(barcode)
        
    w = Path(__file__).with_name('weight.txt')
    with open(w, "w") as file:
        file.write(str(weight))
        


while True:
    log('dafsgsgsg',4)