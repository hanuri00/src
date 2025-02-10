# -*- coding: utf-8 -*-
# update : {current_date}

from zeroCar import rightWheel, leftWheel
from time import sleep
from datetime import datetime
import curses

# 현재 날짜를 문자열로 가져오기
current_date = datetime.now().strftime("%Y%m%d")

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
    move_wheels(speed * 0.7, speed, duration)

def go_right(speed, duration=None):
    move_wheels(speed, speed * 0.7, duration)

def stop():
    leftWheel.stop()
    rightWheel.stop()

def main(window):
    # curses 초기화
    curses.cbreak()
    window.keypad(True)
    window.nodelay(True)

    while True:
        key = window.getch()

        if key == ord('w'):
            # w가 눌렸을 때 다음 입력을 읽는다
            next_key = window.getch()
            if next_key == ord('a'):  # w와 a가 동시에 눌렸는지 확인
                go_left(1)
            elif next_key == ord('d'):  # w와 d가 동시에 눌렸는지 확인
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

if __name__ == "__main__":
    curses.wrapper(main)
