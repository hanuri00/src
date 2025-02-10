from zeroCar import rightWheel, leftWheel
from time import sleep

def move_wheels(left_speed, right_speed, duration=None): # 중복 코드 제거
    leftWheel.forward(speed=left_speed) if left_speed > 0 else leftWheel.backward(speed=abs(left_speed))
    rightWheel.forward(speed=right_speed) if right_speed > 0 else rightWheel.backward(speed=abs(right_speed))
    if duration:
        sleep(duration)
        stop()

def go(speed, duration=None):
    move_wheels(speed, speed, duration)

def back(speed, duration=None):
    move_wheels(-speed, -speed, duration) # 음수 속도로 backward

def turn_left(speed, duration=None):
    move_wheels(-speed, speed, duration)  # Robot의 left() 메서드와 동일한 효과

def turn_right(speed, duration=None):
    move_wheels(speed, -speed, duration)  # Robot의 right() 메서드와 동일한 효과

def go_left(speed, duration=None):
    move_wheels(speed*0.7, speed, duration) # curve 효과를 주기 위해 속도 조절

def go_right(speed, duration=None):
    move_wheels(speed, speed*0.7, duration) # curve 효과를 주기 위해 속도 조절

def stop():
    leftWheel.stop()
    rightWheel.stop()

try:
    while True:
        go(1, 2)
        sleep(0.5)
        back(0.8, 2)
        sleep(0.5)
        turn_left(1, 1)
        sleep(0.5)
        turn_right(1, 1)
        sleep(0.5)
        go_left(1, 2)
        sleep(0.5)
        go_right(1, 2)
        sleep(0.5)

except KeyboardInterrupt:
    stop()
    print("finished!!")