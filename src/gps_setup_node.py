#!/usr/bin/env python
# license removed for brevity
import rospy
import serial
import time
from std_msgs.msg import String

def gpsSetup():
    ser = serial.Serial('/dev/ttyUSB0',9600)
    ser.write(b'\$PMTK251,115200*1F\r\n')
    rospy.sleep(1.)
    ser.close()
    ser = serial.Serial('/dev/ttyUSB0',115200)
    ser.write(b'\$PMTK220,100*2F\r\n')
    rospy.sleep(1.)
    ser.close()
    
    rospy.init_node('gpsSetup', anonymous=True)
    
    msg_str = "GPS set to 115200bauds to 100Hz %s" % rospy.get_time()
    rospy.loginfo(msg_str)

if __name__ == '__main__':
    try:
        gpsSetup()
    except rospy.ROSInterruptException:
        pass