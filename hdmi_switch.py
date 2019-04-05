# rpi gpio
#
#
# Kirk Vasilas
#
import RPi.GPIO as GPIO
import time

#RPi = 1
#Wii = 2
#xbox = 3

def current_state():
    #state = read pins to determine if hdmi switcher is in point 1, 2, 3
    #3 indicator wires to 3 pins
    #poll pins for high or low
    p1 = 0 #RPi
    p2 = 0 #wii
    p3 = 0 #xbox
    high = 1
    #assumes one will always be high
    if(p1 = high):
        return(1)
    elif(p2 = high):
        return(2)
    else:
        return(3)

def button_press():
    #one press of a button
    #send pulse to switch button
    #gpio pin high
    #time pause
    #gpio pin low
    pass

def switch_input(target):
    current = current_state()
    while(target != current):
        button_press()
        current = current_state()
    return 0


def switch_input_a(target):
    current = current_state()
    if(current == target):
        print("no press")
        print("same")
        return 0
    else:
        if(target == current + 1):
            button_press()
            print('one press')
            print('1-2', '2-3', '3-1', sep=' / ')
        elif(target == current - 1):
            button_press()
            button_press()
            print('two press')
            print('2-1', '3-2')
        else:
            button_press()
            button_press()
            print('two press')
            print('1-3')
    return 0
