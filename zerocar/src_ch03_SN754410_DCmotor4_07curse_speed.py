#-*- coding: utf-8 -*-
from zeroCar import rightWheel, leftWheel
from time import sleep
import curses

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
    speed = 0.5  # 초기 속도 설정

    while True:
        key = window.getch()

        if key == ord('w'):
            go(speed)
            while True: # w 키가 눌려있는 동안
                key2 = window.getch()
                if key2 == ord('+'):
                    speed = min(1, speed + 0.1)
                    print(f"Speed: {speed:.1f}")
                elif key2 == ord('-'):
                    speed = max(0, speed - 0.1)
                    print(f"Speed: {speed:.1f}")
                elif key2 != -1 and key2 != ord('w'): # 다른 키가 눌리면 w 누르기 종료
                    break
        elif key == ord('s'):
            back(speed)
            while True: # s 키가 눌려있는 동안
                key2 = window.getch()
                if key2 == ord('+'):
                    speed = min(1, speed + 0.1)
                    print(f"Speed: {speed:.1f}")
                elif key2 == ord('-'):
                    speed = max(0, speed - 0.1)
                    print(f"Speed: {speed:.1f}")
                elif key2 != -1 and key2 != ord('s'): # 다른 키가 눌리면 s 누르기 종료
                    break
        elif key == ord('a'):
            turn_left(speed)
            while True: # a 키가 눌려있는 동안
                key2 = window.getch()
                if key2 == ord('+'):
                    speed = min(1, speed + 0.1)
                    print(f"Speed: {speed:.1f}")
                elif key2 == ord('-'):
                    speed = max(0, speed - 0.1)
                    print(f"Speed: {speed:.1f}")
                elif key2 != -1 and key2 != ord('a'): # 다른 키가 눌리면 a 누르기 종료
                    break
        elif key == ord('d'):
            turn_right(speed)
            while True: # d 키가 눌려있는 동안
                key2 = window.getch()
                if key2 == ord('+'):
                    speed = min(1, speed + 0.1)
                    print(f"Speed: {speed:.1f}")
                elif key2 == ord('-'):
                    speed = max(0, speed - 0.1)
                    print(f"Speed: {speed:.1f}")
                elif key2 != -1 and key2 != ord('d'): # 다른 키가 눌리면 d 누르기 종료
                    break
        elif key == ord('q'):
            break
        else:
            stop()

        sleep(0.1)

curses.wrapper(main)