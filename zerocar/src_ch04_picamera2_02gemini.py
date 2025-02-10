# -*- coding: utf-8 -*-
# update : {current_date}

from gpiozero import Robot, Motor
from time import sleep
from datetime import datetime
import curses
from picamera2 import Picamera2
import os

current_date = datetime.now().strftime("%Y%m%d")

rightWheel = Robot(Motor(21, 20), Motor(26, 19))
leftWheel = Robot(Motor(23, 24), Motor(22, 27))

image_dir = f'line_images_{current_date}'
os.makedirs(image_dir, exist_ok=True)

cam = Picamera2()

def move_wheels(left_speed, right_speed, duration=None):
    leftWheel.forward(speed=left_speed) if left_speed > 0 else leftWheel.backward(speed=abs(left_speed))
    rightWheel.forward(speed=right_speed) if right_speed > 0 else rightWheel.backward(speed=abs(right_speed))
    if duration:
        sleep(duration)
        stop()

def go(speed, duration=None):
    move_wheels(speed, speed, duration)
    return "forward"

def back(speed, duration=None):
    move_wheels(-speed, -speed, duration)
    return "backward"

def turn_left(speed, duration=None):
    move_wheels(-speed, speed, duration)
    return "turn_left"

def turn_right(speed, duration=None):
    move_wheels(speed, -speed, duration)
    return "turn_right"

def go_left(speed, duration=None):
    move_wheels(speed * 0.7, speed, duration)
    return "go_left"

def go_right(speed, duration=None):
    move_wheels(speed, speed * 0.7, duration)
    return "go_right"

def stop():
    leftWheel.stop()
    rightWheel.stop()

def capture_image(label):
    try:
        image_path = os.path.join(image_dir, f'lane_image_{datetime.now().strftime("%Y%m%d_%H%M%S")}_{label}.jpg')
        cam.capture(image_path)
        print(f"Image captured: {image_path}")
    except Exception as e:
        print(f"Error capturing image: {e}")

def main(window):
    cam.start()
    window.nodelay(True)

    try:
        while True:
            key = window.getch()

            if key == ord('w'):
                label = go(1)
                capture_image(label)
            elif key == ord('s'):
                label = back(1)
                capture_image(label)
            elif key == ord('a'):
                label = turn_left(1)
                capture_image(label)
            elif key == ord('d'):
                label = turn_right(1)
                capture_image(label)
            elif key == ord('q'):
                break
            else:
                stop()

            sleep(0.1)
    finally:
        stop()
        cam.close()

if __name__ == "__main__":
    curses.wrapper(main)