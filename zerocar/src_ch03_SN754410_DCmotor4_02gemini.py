#-*- coding: utf-8 -*-

from gpiozero import Robot
from time import sleep

robot = Robot(left=(23, 24), right=(21, 20))  # Robot 객체 생성

def go(speed, duration=None):  # duration 추가 (초 단위)
    robot.forward(speed=speed)
    if duration:
        sleep(duration)
        robot.stop()

def back(speed, duration=None): # duration 추가 (초 단위)
    robot.backward(speed=speed)
    if duration:
        sleep(duration)
        robot.stop()

def turn_left(speed, duration=None): # turn_left로 이름 변경
    robot.left(speed=speed) # Robot 클래스의 left() 메서드 사용
    if duration:
        sleep(duration)
        robot.stop()

def turn_right(speed, duration=None): # turn_right로 이름 변경
    robot.right(speed=speed) # Robot 클래스의 right() 메서드 사용
    if duration:
        sleep(duration)
        robot.stop()

def go_left(speed, duration=None):
    robot.forward(speed=speed, curve_left=0.5) # curve_left 사용
    if duration:
        sleep(duration)
        robot.stop()

def go_right(speed, duration=None):
    robot.forward(speed=speed, curve_right=0.5) # curve_right 사용
    if duration:
        sleep(duration)
        robot.stop()


def stop():
    robot.stop()

try:
    while True:
        go(0.8, 2) # 속도 0.8, 2초 동안 이동 후 정지
        sleep(0.5)
        back(0.8, 2)
        sleep(0.5)
        turn_left(0.7, 2) # 속도 0.7, 2초 동안 회전 후 정지
        sleep(0.5)
        turn_right(0.7, 2)
        sleep(0.5)
        go_left(0.8, 2)
        sleep(0.5)
        go_right(0.8, 2)
        sleep(0.5)

except KeyboardInterrupt:
    stop()
    print("finished!!")