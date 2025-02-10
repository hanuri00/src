# zeroCar.py

from gpiozero import Robot, Motor

motor1 = Motor(26, 19)       # right_front 1    ok
motor2 = Motor(27, 22)       # right_rear 2     ok
motor3 = Motor(21, 20)       # left_front 3     ok
motor4 = Motor(24, 23)       # left_rear 4      ok

rightWheel = Robot(motor1, motor2)
leftWheel = Robot(motor3, motor4)
