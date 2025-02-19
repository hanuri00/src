# -*- coding: utf-8 -*-
# update : {current_date}
# author : hanuri00
# description : zeroCar Project - Collect images of the lane lines

# Import necessary libraries
import cv2
import numpy as np
import os
from datetime import datetime
from picamera2 import Picamera2
from time import sleep
from zeroCar import rightWheel, leftWheel

# Create a directory to save images
image_dir = '/home/pi/zeroCar/line_images'
if not os.path.exists(image_dir):
    os.makedirs(image_dir)

#datetime
current_date = datetime.now().strftime("%Y%m%d")

# Initialize the camera
cam = Picamera2()
cam.configure(cam.create_preview_configuration(main={"size": (640, 480)}))
cam.start()

# Define the speed and turn factor
speed = 1
turn_factor = 0.7

# Define the function to move the wheels
def move_wheels(left_speed, right_speed, duration=None):
    leftWheel.forward(speed=left_speed) if left_speed > 0 else leftWheel.backward(speed=abs(left_speed))
    rightWheel.forward(speed=right_speed) if right_speed > 0 else rightWheel.backward(speed=abs(right_speed))
    if duration:
        sleep(duration)
        stop()

# Define the function to move the zeroCar forward
def go(speed, duration=None):
    move_wheels(speed, speed, duration)
    return 'go'

def back(speed, duration=None):
    move_wheels(-speed, -speed, duration)
    return 'back'

def turn_left(speed, duration=None):
    move_wheels(-speed, speed, duration)
    return 'turn_left'

def turn_right(speed, duration=None):
    move_wheels(speed, -speed, duration)
    return 'turn_right'

def go_left(speed, duration=None):
    move_wheels(speed * turn_factor, speed, duration)
    return 'go_left'

def go_right(speed, duration=None):
    move_wheels(speed, speed * turn_factor, duration)
    return 'go_right'

def stop():
    leftWheel.stop()
    rightWheel.stop()
    return 'stop'

# Define the function to capture an image
def capture_image(label):
    try:
        imgcnt = 0
        image_path = os.path.join(image_dir, f'{imgcnt}_line_image_{datetime.now().strftime("%Y%m%d_%H%M%S")}_{label}.jpg')
        sleep(0.1)
        rawCapture = cam.capture_array()
        cv2.imwrite(image_path, rawCapture)
        print(f'Captured image: {image_path}')
        imgcnt += 1
    except Exception as e:
        print(f'Error: {e}')
    
# Define the turn factor
def set_turn_factor(factor):
    global turn_factor
    new_turn_factor = turn_factor + factor
    if 0.1 <= new_turn_factor <= 1.0:
        turn_factor = new_turn_factor
    else:
        print('Invalid turn factor. The turn factor should be between 0.1 and 1.0.')

# Define the main function
def main():
    last_capture_time = datetime.now()

    while True:
        key = cv2.waitKey(1) & 0xFF

        if key == ord('w'):
            label = 'go'
            if (datetime.now() - last_capture_time).seconds >= 2:
                capture_image(label)
                last_capture_time = datetime.now()
        elif key == ord('s'):
            label = 'back'
            if (datetime.now() - last_capture_time).seconds >= 2:
                capture_image(label)
                last_capture_time = datetime.now()
        elif key == ord('a'):
            label = 'turn_left'
            if (datetime.now() - last_capture_time).seconds >= 2:
                capture_image(label)
                last_capture_time = datetime.now()
        elif key == ord('d'):
            label = 'turn_right'
            if (datetime.now() - last_capture_time).seconds >= 2:
                capture_image(label)
                last_capture_time = datetime.now()
        elif key == ord('q'):
            label = 'go_left'
            if (datetime.now() - last_capture_time).seconds >= 2:
                capture_image(label)
                last_capture_time = datetime.now()
        elif key == ord('e'):
            label = 'go_right'
            if (datetime.now() - last_capture_time).seconds >= 2:
                capture_image(label)
                last_capture_time = datetime.now()
        elif key == ord('+'):
            set_turn_factor(0.1)
        elif key == ord('-'):
            set_turn_factor(-0.1)
        elif key == 27:  # ESC 키를 누르면 루프 종료
            break
        else:
            stop()

        sleep(0.1)
    
    stop()
    cam.stop()

if __name__ == '__main__':
    main()
