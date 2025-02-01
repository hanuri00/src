#-*- coding: utf-8 -*-

from gpiozero import Robot, Motor
from time import sleep
import keyboard
import os
import subprocess
from datetime import datetime

frontWheel = Robot(left=(6, 13), right=(12, 16))
rearWheel = Robot(left=(19, 26), right=(20, 21))

base_data_dir = "/home/pi/images"
os.makedirs(base_data_dir, exist_ok=True)

def go():
    frontWheel.forward()
    rearWheel.forward()

def back():
    frontWheel.backward()
    rearWheel.backward()

def left():
    frontWheel.left()
    rearWheel.left()

def right():
    frontWheel.right()
    rearWheel.right()

def go_left():
    frontWheel.forward(speed=1, curve_left=0.6)
    rearWheel.forward(speed=1, curve_left=0.6)

def go_right():
    frontWheel.forward(speed=1, curve_right=0.5)
    rearWheel.forward(speed=1, curve_right=0.5)

def stop():
    frontWheel.stop()
    rearWheel.stop()

try:
    while True:
        now = datetime.now().strftime("%Y%m%d_%H%M%S_%f")[:-3]

        if keyboard.is_pressed('w') and keyboard.is_pressed('a'):
            direction_dir = os.path.join(base_data_dir, "forward_left")
            os.makedirs(direction_dir, exist_ok=True)
            filename = os.path.join(direction_dir, f"forward_left_{now}.jpg")
            go_left()
            subprocess.run(["rpicam-jpeg", "-o", filename])

        elif keyboard.is_pressed('w') and keyboard.is_pressed('d'):
            direction_dir = os.path.join(base_data_dir, "forward_right")
            os.makedirs(direction_dir, exist_ok=True)
            filename = os.path.join(direction_dir, f"forward_right_{now}.jpg")
            go_right()
            subprocess.run(["rpicam-jpeg", "-o", filename])

        elif keyboard.is_pressed('w'):
            direction_dir = os.path.join(base_data_dir, "forward")
            os.makedirs(direction_dir, exist_ok=True)
            filename = os.path.join(direction_dir, f"forward_{now}.jpg")
            go()
            subprocess.run(["rpicam-jpeg", "-o", filename])

        elif keyboard.is_pressed('s'):
            direction_dir = os.path.join(base_data_dir, "backward")
            os.makedirs(direction_dir, exist_ok=True)
            filename = os.path.join(direction_dir, f"backward_{now}.jpg")
            back()
            subprocess.run(["rpicam-jpeg", "-o", filename])

        elif keyboard.is_pressed('a'):
            direction_dir = os.path.join(base_data_dir, "left")
            os.makedirs(direction_dir, exist_ok=True)
            filename = os.path.join(direction_dir, f"left_{now}.jpg")
            left()
            subprocess.run(["rpicam-jpeg", "-o", filename])

        elif keyboard.is_pressed('d'):
            direction_dir = os.path.join(base_data_dir, "right")
            os.makedirs(direction_dir, exist_ok=True)
            filename = os.path.join(direction_dir, f"right_{now}.jpg")
            right()
            subprocess.run(["rpicam-jpeg", "-o", filename])

        elif keyboard.is_pressed('space'):
            stop()
        
        sleep(0.1)

except KeyboardInterrupt:
    stop()
    print("finished!!")