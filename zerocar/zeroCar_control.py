# -*- coding: utf-8 -*-
# update : {current_date}
# author : hanuri00
# description : zeroCar Project - Control
# zeroCar_control.py

import cv2
import numpy as np
from zeroCar import rightWheel, leftWheel
from zeroCar_AI import get_prediction_image  # zeroCar_AI에서 예측 함수 가져오기

# 차선 감지 결과 분석 함수
def analyze_lane(prediction_image):
    height, width = prediction_image.shape
    midpoint = width // 2

    # 이미지의 좌우 절반을 나누어 각각의 차선 중앙을 찾음
    left_half = prediction_image[:, :midpoint]
    right_half = prediction_image[:, midpoint:]

    # 각 절반에서 차선이 있는 픽셀의 x 좌표의 평균값을 계산
    left_lane_center = np.mean(np.where(left_half == 255)[1])
    right_lane_center = np.mean(np.where(right_half == 255)[1]) + midpoint

    # 도로의 중앙 계산
    lane_center = (left_lane_center + right_lane_center) // 2
    return lane_center, midpoint

# zeroCar 제어 로직 함수
def control_zeroCar(lane_center, midpoint):
    if lane_center < midpoint - 20:
        # 왼쪽으로 이동
        leftWheel.backward()
        rightWheel.forward()
    elif lane_center > midpoint + 20:
        # 오른쪽으로 이동
        leftWheel.forward()
        rightWheel.backward()
    else:
        # 직진
        leftWheel.forward()
        rightWheel.forward()

# 메인 실행 코드
if __name__ == "__main__":
    while True:
        prediction_image = get_prediction_image()

        # 차선 감지 결과 해석
        lane_center, midpoint = analyze_lane(prediction_image)

        # zeroCar 제어
        control_zeroCar(lane_center, midpoint)

        # 차선 감지 결과 출력
        cv2.imshow("Prediction", prediction_image)

        # 'q' 키를 누르면 루프 종료
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cv2.destroyAllWindows()
