#-*- coding: utf-8 -*-

from zeroCar import rightWheel, leftWheel
from time import sleep

def go(speed):
    rightWheel.forward(speed=speed)
    leftWheel.forward(speed=speed)

def back(speed):
    rightWheel.backward(speed=speed)
    leftWheel.backward(speed=speed)

def turn_left(speed):
    rightWheel.forward(speed=speed)
    leftWheel.backward(speed=speed)

def turn_right(speed):
    rightWheel.backward(speed=speed)
    leftWheel.forward(speed=speed)
    
def go_left(speed):
    rightWheel.forward(speed=speed)
    leftWheel.forward(speed=speed*0.5)
    
def go_right(speed):
    rightWheel.forward(speed=speed*0.5)
    leftWheel.forward(speed=speed)

def stop():
    rightWheel.stop()
    leftWheel.stop()

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
        turn_left(1)
        sleep(2)
        stop()
        sleep(0.5)
        turn_right(1)
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