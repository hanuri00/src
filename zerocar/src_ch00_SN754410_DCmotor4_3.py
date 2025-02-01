#-*- coding: utf-8 -*-

from gpiozero import Robot, Motor
from time import sleep

frontWheel = Robot(left=(6, 13), right=(12, 16))
rearWheel = Robot(left=(19, 26), right=(20, 21))

def go():
    frontWheel.forward()
    rearWheel.forward()

def back():
    frontWheel.backward()
    rearWheel.backward()

def left():
    frontWheel.left()
    rearWheel.left()

def right():
    frontWheel.right()
    rearWheel.right()

def go_left():
    frontWheel.forward(speed=1, curve_left=0.6)
    rearWheel.forward(speed=1, curve_left=0.6)

def go_right():
    frontWheel.forward(speed=1, curve_right=0.5)
    rearWheel.forward(speed=1, curve_right=0.5)

def stop():
    frontWheel.stop()
    rearWheel.stop()

try:
    while True:
        go()
        sleep(2)
        stop()
        sleep(0.5)
        back()
        sleep(2)
        stop()
        sleep(0.5)
        left()
        sleep(2)
        stop()
        sleep(0.5)
        right()
        sleep(2)
        stop()
        sleep(0.5)
        go_left()
        sleep(2)
        stop()
        sleep(0.5)
        go_right()
        sleep(2)
        stop()
    
        sleep(0.1)

except KeyboardInterrupt:
    stop()
    print("finished!!")