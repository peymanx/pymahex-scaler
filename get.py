import serial
serialData = serial.Serial('/dev/ttyACM0',115200) 

try:    
    # Body of data acquisition code
    while True:
        line = serialData.read(12); # stream is 325 bytes long ,  last byte is a 0x011
        # first 4 bytes are time in msec
        Ttemp = array.array("I",line[0:4]);  # extracts time the I, uint32_t millis
        currT = Ttemp[0]/1000.0; # writes single element array to variable
        print "Time = ",currT
        # extracts the array of h, int16_t variable
        tempArray = array.array("h",line[4:324]); s
        print "tempArray ="
        print tempArray
except:
    ...