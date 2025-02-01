#-*- coding: utf-8 -*-

from gpiozero import Robot, Motor
from time import sleep

leftWheel = Robot(left=(6, 13), right=(12, 16))
rightWheel = Robot(left=(19, 26), right=(20, 21))

def go(speed):
    rightWheel.forward(speed=speed)
    leftWheel.forward(speed=speed)

def back(speed):
    rightWheel.backward(speed=speed)
    leftWheel.backward(speed=speed)

def left(speed):
    rightWheel.forward(speed=speed)
    leftWheel.forward(speed=0)

def right(speed):
    rightWheel.forward(speed=0)
    leftWheel.forward(speed=speed)
    

def go_left(speed):
    rightWheel.forward(speed=speed)
    leftWheel.forward(speed=speed*0.5)
    

def go_right(speed):
    rightWheel.forward(speed=speed*0.5)
    leftWheel.forward(speed=speed)

def stop():
    leftWheel.stop()
    rightWheel.stop()

try:
    while True:
        go(1)
        sleep(2)
        stop()
        sleep(0.5)
        back(1)
        sleep(2)
        stop()
        sleep(0.5)
        left(1)
        sleep(2)
        stop()
        sleep(0.5)
        right(1)
        sleep(2)
        stop()
        sleep(0.5)
        go_left(1)
        sleep(2)
        stop()
        sleep(0.5)
        go_right(1)
        sleep(2)
        stop()
    
        sleep(0.1)

except KeyboardInterrupt:
    stop()
    print("finished!!")