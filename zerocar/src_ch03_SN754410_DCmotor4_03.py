#-*- coding: utf-8 -*-
# update 20250202

from gpiozero import Robot, Motor
from time import sleep

#motor = Motor(21, 20)       # right_front 1    ok
#motor = Motor(26, 19)       # right_rear 2     ok
#motor = Motor(23, 24)       # left_front 3     ok
#motor = Motor(22, 27)       # left_rear 4      ok

rightWheel = Robot(Motor(21, 20), Motor(26, 19))
leftWheel = Robot(Motor(23, 24), Motor(22, 27))

#robot = Robot(left=(23, 24), right=(21, 20))  # Robot 객체 생성, gemini가 추천해줌. 아니지.. 

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
        go(1, 2) # 속도 0.8, 2초 동안 이동 후 정지
        sleep(0.5)
        back(0.8, 2)
        sleep(0.5)
        turn_left(1, 1) # 속도 0.7, 2초 동안 회전 후 정지
        sleep(0.5)
        turn_right(1, 1)
        sleep(0.5)
        go_left(1, 2)
        sleep(0.5)
        go_right(1, 2)
        sleep(0.5)

except KeyboardInterrupt:
    stop()
    print("finished!!")