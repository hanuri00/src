# -*- coding: utf-8 -*-
# update : {current_date}

from zeroCar import rightWheel, leftWheel
from time import sleep
from datetime import datetime
import curses

# Get the current date as a string
current_date = datetime.now().strftime("%Y%m%d")

def move_wheels(left_speed, right_speed, duration=None):
    # Move the wheels based on the given speeds
    leftWheel.forward(speed=left_speed) if left_speed > 0 else leftWheel.backward(speed=abs(left_speed))
    rightWheel.forward(speed=right_speed) if right_speed > 0 else rightWheel.backward(speed=abs(right_speed))
    if duration:
        sleep(duration)
        stop()

def go(speed, duration=None):
    # Move forward at the given speed
    move_wheels(speed, speed, duration)

def back(speed, duration=None):
    # Move backward at the given speed
    move_wheels(-speed, -speed, duration)

def turn_left(speed, duration=None):
    # Turn left by moving the left wheel backward
    move_wheels(-speed, speed, duration)

def turn_right(speed, duration=None):
    # Turn right by moving the right wheel backward
    move_wheels(speed, -speed, duration)

def go_left(speed, duration=None):
    # Move diagonally left
    move_wheels(speed * 0.7, speed, duration)

def go_right(speed, duration=None):
    # Move diagonally right
    move_wheels(speed, speed * 0.7, duration)

def stop():
    # Stop both wheels
    leftWheel.stop()
    rightWheel.stop()

def main(window):
    # Initialize curses
    curses.cbreak()
    window.keypad(True)
    window.nodelay(True)

    while True:
        key = window.getch()

        if key == ord('w'):
            # Check the next key after 'w'
            next_key = window.getch()
            if next_key == ord('a'):  # Check if 'a' is pressed with 'w'
                go_left(1)
            elif next_key == ord('d'):  # Check if 'd' is pressed with 'w'
                go_right(1)
            else:
                go(1)  # Only 'w' is pressed
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
