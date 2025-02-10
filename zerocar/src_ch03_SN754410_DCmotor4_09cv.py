# -*- coding: utf-8 -*-
# update : {current_date}

from zeroCar import rightWheel, leftWheel
from time import sleep
import cv2
import numpy as np
from datetime import datetime

# 현재 날짜를 문자열로 가져오기
current_date = datetime.now().strftime("%Y%m%d")

# 주석에 현재 날짜 삽입
print(f"# update {current_date}")

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

def main():
    cv2.namedWindow("Control Window")

    while True:
        img = np.zeros((300, 600, 3), dtype=np.uint8)
        cv2.putText(img, "Press 'w' to go forward", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
        cv2.putText(img, "Press 's' to go backward", (50, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
        cv2.putText(img, "Press 'a' to turn left", (50, 150), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
        cv2.putText(img, "Press 'd' to turn right", (50, 200), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
        cv2.putText(img, "Press 'q' to quit", (50, 250), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

        cv2.imshow("Control Window", img)

        key = cv2.waitKey(100)

        if key == ord('w'):
            go(1)
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

    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
