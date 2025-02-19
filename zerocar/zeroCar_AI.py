# -*- coding: utf-8 -*-
# update : {current_date}
# author : hanuri00
# description : zeroCar Project - AI
# zeroCar_AI.py 

import cv2
import numpy as np
import onnxruntime as ort
from picamera.array import PiRGBArray
from picamera import PiCamera

# ONNX 모델 로드
ort_session = ort.InferenceSession('/home/pi/zeroCar/lane_detection_model.onnx')

# 카메라 초기화
camera = PiCamera()
camera.resolution = (640, 480)
rawCapture = PiRGBArray(camera, size=(640, 480))

def get_prediction_image():
    for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
        image = frame.array
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        resized_image = cv2.resize(gray, (256, 256))
        input_image = np.expand_dims(resized_image, axis=(0, -1)).astype(np.float32)

        # 모델 예측
        onnx_inputs = {ort_session.get_inputs()[0].name: input_image}
        onnx_outputs = ort_session.run(None, onnx_inputs)
        prediction = onnx_outputs[0]
        prediction_image = (prediction[0, 0, :, :] > 0.5).astype(np.uint8) * 255

        rawCapture.truncate(0)
        
        return prediction_image

    camera.close()
    cv2.destroyAllWindows()
