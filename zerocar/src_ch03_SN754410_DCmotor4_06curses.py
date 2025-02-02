#-*- coding: utf-8 -*-
# update 20250202

from gpiozero import Robot, Motor
from time import sleep
import curses

rightWheel = Robot(Motor(21, 20), Motor(26, 19))
leftWheel = Robot(Motor(23, 24), Motor(22, 27))

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

def main(window):
    window.nodelay(True)

    while True:
        key = window.getch()

        if key == ord('w'):
            if window.getch() == ord('a'):  # w와 a가 동시에 눌렸는지 확인
                go_left(1)
            elif window.getch() == ord('d'):  # w와 d가 동시에 눌렸는지 확인
                go_right(1)
            else:
                go(1)  # w만 눌렸을 경우
        elif key == ord('s'):
            back(1)
        elif key == ord('a'):
            turn_left(1)
        elif key == ord('d'):
            turn_right(1)
        elif key == ord('q'):
            break
        else:
            stop()

        sleep(0.1)

curses.wrapper(main)