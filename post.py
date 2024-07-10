import sys

if len(sys.argv)>1:
    barcode = sys.argv[1]
    print("""
    [
        {
            \"parcelId\": \"{barcode}\",
            \"length\": 1,
            \"width\": 2,
            \"height\": 3,
            \"grossWeight\": 1.0,
            \"scannedOn\": \"2024-04-22T10:32:00\"
        }
    ]  sent!""")
    if barcode == 'SHP3352120467-1':    
        print("""
        Response: 
        [
            {
                \"parcelId\": \"{barcode}\",
                \"cityCode\": \"IR-ZHDN\"
            }
        ]
            
        """)
else:
    print("[]")

