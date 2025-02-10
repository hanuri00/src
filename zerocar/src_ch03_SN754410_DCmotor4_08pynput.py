#-*- coding: utf-8 -*-
# update 20250204
#GUI 환경이 아닐경우 에러..

from zeroCar import rightWheel, leftWheel
from time import sleep
from pynput import keyboard

def move_wheels(left_speed, right_speed, duration=None):
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

speed = 0.5  # 초기 속도 설정

def on_press(key):
    global speed  # 전역 변수 speed 사용 선언
    try:
        if key.char == 'w':
            go(speed)
        elif key.char == 's':
            back(speed)
        elif key.char == 'a':
            turn_left(speed)
        elif key.char == 'd':
            turn_right(speed)
        elif key.char == '+':
            speed = min(1, speed + 0.1)
            print(f"Speed: {speed:.1f}")
        elif key.char == '-':
            speed = max(0, speed - 0.1)
            print(f"Speed: {speed:.1f}")
    except AttributeError:
        if key == keyboard.Key.space:
            stop()

def on_release(key):
    try:
        if key.char in ['w', 's', 'a', 'd']:
            stop()
    except AttributeError:
        pass

with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()  