import requests,json, sys,datetime
from pathlib import Path
from enum import Enum
from color import *

class ApiResult(Enum):
    TEHRAN = 1
    PROVIDENCE = 2
    REJECT = 3
    ERROR = -1

url = "http://172.24.24.59:8011/v1/parcels/scan"


p = Path(__file__).with_name('database.txt')
tehran_db = p.read_text().splitlines()

def is_tehran(text):
    for city in tehran_db:
        if text.__contains__(city): return True
    return False

def send_to_ecourier(barcode, weight):
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
    
    
    print('Data to send:', color=print.HIGHLIGHTED_YELLOW)
    json_object = json.loads(payload)
    json_formatted_str = json.dumps(json_object, indent=2)
    print(json_formatted_str)
    
    
    headers = {
    'authorization': 'Basic amFsSkh6VlN2QnlNQkNXRnNNcVJVZjdQU3lDQ2ZhZExBNU51bmlIc3dFNGVlcVpyOg==',
    'Content-Type': 'application/json'
    }

    try:
        response = requests.request("POST", url, headers=headers, data=payload)

        print('E-Courier Answer:', color=print.HIGHLIGHTED_YELLOW)            
        if response.status_code == 200 and response.text.__contains__(barcode):
            json_object = json.loads(response.text)
            json_formatted_str = json.dumps(json_object, indent=2)
            print(json_formatted_str)
            if is_tehran(response.text):
                print('Tehran', color=print.HIGHLIGHTED_GREEN)
                return ApiResult.TEHRAN
            else:
                print('Providence', color=print.HIGHLIGHTED_GREEN)
                return ApiResult.PROVIDENCE
        elif response.text == '[]':
            print(response.text)                
            print('Parcel Rejected', color=print.HIGHLIGHTED_RED)
            return ApiResult.REJECT
        else:
            print('Connection Error', color=print.HIGHLIGHTED_RED)          
            return ApiResult.ERROR
    except:
        print('Connection Error', color=print.HIGHLIGHTED_RED)
        return ApiResult.ERROR
        
    


if __name__ == '__main__':
    if len(sys.argv)>1:
        barcode = sys.argv[1]
        send_to_ecourier(barcode, 5)