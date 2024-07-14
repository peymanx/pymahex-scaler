import sys
from color import * 
import requests
import json

url = "http://172.24.24.59:8011/v1/parcels/scan"

payload = json.dumps([
  {
    "parcelId": "SHP3352120467-1",
    "length": 1,
    "width": 2,
    "height": 3,
    "grossWeight": 1,
    "scannedOn": "2024-04-22T10:32:00"
  }
])
headers = {
  'authorization': 'Basic amFsSkh6VlN2QnlNQkNXRnNNcVJVZjdQU3lDQ2ZhZExBNU51bmlIc3dFNGVlcVpyOg==',
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
