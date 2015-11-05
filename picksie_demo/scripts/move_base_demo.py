#!/usr/bin/env python
from picksie import *

def Init():
    print "*******************************"
    print "VISION TRACKING DEMO - Main vision tracking demo script"
    print "*******************************"
    #Initialise the youbot object
    youbot = Youbot()

    #Drive the youbot
    youbot.DriveTo(10,0,0,0,0,0,1)

    
    #Finally - shutdown the robot
    youbot.Shutdown()


if __name__ == '__main__':
    try:
            Init()
    except rospy.ROSInterruptException:
        pass
