from color import * 
import requests
import json
import datetime


url = "http://172.24.24.59:8011/v1/parcels/scan"

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


get_parcel('SHP3352120467-1', 5)