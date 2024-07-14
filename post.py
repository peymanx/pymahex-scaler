from color import * 
import requests
import json, sys
import datetime
from pathlib import Path

from enum import Enum

class City(Enum):
    TEHRAN = 1
    PROVIDENCE = 2
    REJECT = 3

url = "http://172.24.24.59:8011/v1/parcels/scan"


p = Path(__file__).with_name('database.txt')
tehran_db = p.read_text().splitlines()

def is_tehran(text):
    for city in tehran_db:
        if text.__contains__(city): return True
    return False

def get_parcel(barcode, weight):
    now = datetime.datetime.utcnow().isoformat()
    payload = json.dumps([
    {
        "parcelId": barcode,
        "length": 0,
        "width": 0,
        "height": 0,
        "grossWeight": weight,
        "scannedOn": now
    }
    ])
    headers = {
    'authorization': 'Basic amFsSkh6VlN2QnlNQkNXRnNNcVJVZjdQU3lDQ2ZhZExBNU51bmlIc3dFNGVlcVpyOg==',
    'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.text)
    if response.status_code == 200 and response.text.__contains__(barcode):
        if is_tehran(response.text):
            print('tehran')
            return City.TEHRAN
        else:
            print('providence')
            return City.PROVIDENCE
    else:
        print('reject')
        return City.REJECT
        
    

barcode = sys.argv[1]
get_parcel(barcode, 5)