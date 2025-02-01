

from gpiozero import Robot, Motor
from time import sleep
import curses

frontWheel = Robot(left=(6, 13), right=(12, 16))
rearWheel = Robot(left=(19, 26), right=(20, 21))

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

def main(stdscr):
    stdscr.clear()
    stdscr.nodelay(True)
    stdscr.addstr("Use arrow keys to control the car. Press 'q' to quit.\n")

    while True:
        try:
            key = stdscr.getkey()
            if key == curses.KEY_UP:
                go()
                stdscr.addstr("Forward\n")
            elif key == curses.KEY_DOWN:
                back()
                stdscr.addstr("Backward\n")
            elif key == curses.KEY_LEFT:
                left()
                stdscr.addstr("Left\n")
            elif key == curses.KEY_RIGHT:
                right()
                stdscr.addstr("Right\n")
            elif key == 'q':
                break
            elif key == 'w':
                go_left()
                stdscr.addstr("Forward Left\n")
            elif key == 'e':
                go_right()
                stdscr.addstr("Forward Right\n")
            else:
                stop()
                stdscr.addstr("Stop\n")
            stdscr.refresh()
            sleep(0.1)
        except curses.error:
            pass

curses.wrapper(main)
stop()