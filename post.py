import sys
from color import * 

if len(sys.argv)>1:
    barcode = sys.argv[1]
    print("Data to send:", color=print.HIGHLIGHTED)
    print("""
    [
        {
            \"parcelId\": \"{"""+barcode+"""}\",
            \"length\": 1,
            \"width\": 2,
            \"height\": 3,
            \"grossWeight\": 1.0,
            \"scannedOn\": \"2024-04-22T10:32:00\"
        }
    ] """)
    
    print("Response:", color=print.HIGHLIGHTED)
    if barcode == 'SHP3352120467-1':    
        print("""
        
        [
            {
                \"parcelId\": \"{"""+barcode+"""}\",
                \"cityCode\": \"IR-ZHDN\"
            }
        ]
            
        """)
    else:
        print("[]")
else:
    print("please mention the barcode", color=print.HIGHLIGHTED_RED)
