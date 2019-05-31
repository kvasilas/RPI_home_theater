# Python3
#
# Communication to arduino from media player
# Switches HDMI Inputs
#
# Author: Kirk KC Vasilas
# Created: May 2019
#

from time import *
import serial

#serial Location
#loc = 'COM4' #windows
loc ='/dev/ttyUSB0' #linux

ser = serial.Serial(loc, 9600)

def switch(target):
    m = 1
    x = 2
    w = 3
    if(target == m):
        ser.write(b'1')
        sleep(1)
    elif(target == x):
        ser.write(b'2')
        sleep(1)
    else:
        ser.write(b'3')
        sleep(1)

def check_current():
    ser.write(b'c')
    sleep(1)
    curr = ser.read()
    #parse and pull out the answer

#to do
#optomize switch
