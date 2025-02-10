#-*- coding: utf-8 -*-

from zeroCar import rightWheel, leftWheel
from time import sleep

def go(speed, duration=None):  # duration 추가 (초 단위)
    rightWheel.forward(speed=speed)
    leftWheel.forward(speed=speed)

    if duration:
        sleep(duration)
        stop()

def back(speed, duration=None):
    rightWheel.backward(speed=speed)
    leftWheel.backward(speed=speed)
    if duration:
        sleep(duration)
        stop()

def turn_left(speed, duration=None):
    rightWheel.forward(speed=speed)
    leftWheel.backward(speed=speed)
    if duration:
        sleep(duration)
        stop()

def turn_right(speed, duration=None):
    rightWheel.backward(speed=speed)
    leftWheel.forward(speed=speed)
    if duration:
        sleep(duration)
        stop()

def go_left(speed, duration=None):
    rightWheel.forward(speed=speed)
    leftWheel.forward(speed=speed*0.5)
    if duration:
        sleep(duration)
        stop()

def go_right(speed, duration=None):
    rightWheel.forward(speed=speed*0.5)
    leftWheel.forward(speed=speed)
    if duration:
        sleep(duration)
        stop()


def stop():
    leftWheel.stop()
    rightWheel.stop()

try:
    while True:
        print('go!!!!!')
        go(1, 2) # 속도 0.8, 2초 동안 이동 후 정지
        sleep(0.5)
        print('back!!!!!')
        back(0.8, 2)
        sleep(0.5)
        print('turn left !')
        turn_left(1, 1) # 속도 0.7, 2초 동안 회전 후 정지
        sleep(0.5)
        print('turn right !')
        turn_right(1, 1)
        sleep(0.5)
        print('go left !')
        go_left(1, 2)
        sleep(0.5)
        print('turn right !')
        go_right(1, 2)
        sleep(0.5)

except KeyboardInterrupt:
    stop()
    print("finished!!")