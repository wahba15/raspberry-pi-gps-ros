import serial
import time
ser = serial.Serial('/dev/ttyUSB0',9600)
ser.write(b'\$PMTK251,115200*1F\r\n')
time.sleep(1)
ser.close()
ser = serial.Serial('/dev/ttyUSB0',115200)
ser.write(b'\$PMTK220,100*2F\r\n')
time.sleep(1)
ser.close()