# -*- coding: utf-8 -*-
# update : {current_date}

from zeroCar import rightWheel, leftWheel
from time import sleep
from datetime import datetime
import curses
from picamera2 import Picamera2
import os

current_date = datetime.now().strftime("%Y%m%d")

# Create a directory to save images
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

def capture_image():
    image_path = os.path.join(image_dir, f'line_image_{datetime.now().strftime("%Y%m%d_%H%M%S")}.jpg')
    cam.capture(image_path)

def main(window):
    curses.cbreak()
    window.keypad(True)
    window.nodelay(True)

    cam.start() 

    while True:
        key = window.getch()

        if key == ord('w'):
            next_key = window.getch()
            if next_key == ord('a'):
                go_left(1)
            elif next_key == ord('d'):
                go_right(1)
            else:
                go(1)
                capture_image()  # Capture image while moving forward
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

    stop()
    cam.close()  # Close the camera

if __name__ == "__main__":
    curses.wrapper(main)
