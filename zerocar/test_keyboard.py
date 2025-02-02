#-*- coding: utf-8 -*-
# update 20250202

from gpiozero import Robot, Motor
from time import sleep
import keyboard  # keyboard 라이브러리 임포트

rightWheel = Robot(Motor(21, 20), Motor(26, 19))
leftWheel = Robot(Motor(23, 24), Motor(22, 27))

def move_wheels(left_speed, right_speed, duration=None): # 중복 코드 제거
    leftWheel.forward(speed=left_speed) if left_speed > 0 else leftWheel.backward(speed=abs(left_speed))
    rightWheel.forward(speed=right_speed) if right_speed > 0 else rightWheel.backward(speed=abs(right_speed))
    if duration:
        sleep(duration)
        stop()

def go(speed, duration=None):
    move_wheels(speed, speed, duration)

def back(speed, duration=None):
    move_wheels(-speed, -speed, duration)

def turn_left(speed, duration=None):
    move_wheels(-speed, speed, duration)

def turn_right(speed, duration=None):
    move_wheels(speed, -speed, duration)

def go_left(speed, duration=None):
    move_wheels(speed*0.7, speed, duration)

def go_right(speed, duration=None):
    move_wheels(speed, speed*0.7, duration)

def stop():
    leftWheel.stop()
    rightWheel.stop()

try:
    while True:
        if keyboard.is_pressed('w') and keyboard.is_pressed('a'):  # w와 a 키가 동시에 눌렸을 때
            go_left(1)
        elif keyboard.is_pressed('w') and keyboard.is_pressed('d'):  # w와 d 키가 동시에 눌렸을 때
            go_right(1)
        elif keyboard.is_pressed('w'):
            go(1)
        elif keyboard.is_pressed('s'):
            back(1)
        elif keyboard.is_pressed('a'):
            turn_left(1)
        elif keyboard.is_pressed('d'):
            turn_right(1)
        else:
            stop()  # 아무 키도 눌리지 않았을 때는 정지

        sleep(0.1)  # 키 입력 감지 간격

except KeyboardInterrupt:
    stop()
    print("finished!!")