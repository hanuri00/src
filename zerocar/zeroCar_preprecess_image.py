# zeroCar_preprocess_image.py

import os
import cv2
import numpy as np
from keras.preprocessing.image import ImageDataGenerator

def preprocess_image(image_path):
    # 이미지 로드
    image = cv2.imread(image_path)
    if image is None:
        raise ValueError(f"이미지를 로드할 수 없습니다: {image_path}")

    # ROI 설정 – 아랫쪽 1/2
    height, width, _ = image.shape
    roi = image[int(height/2):height, 0:width]  # 하단 절반

    # 색상 공간 변환 (BGR to HSV)
    image_hsv = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)

    # 그레이 스케일 변환
    gray_image = cv2.cvtColor(image_hsv, cv2.COLOR_HSV2BGR)
    gray_image = cv2.cvtColor(gray_image, cv2.COLOR_BGR2GRAY)

    # 블러링
    blurred_image = cv2.GaussianBlur(gray_image, (5, 5), 0)

    # 에지 검출
    edges = cv2.Canny(blurred_image, 50, 150)

    # 임계값 설정
    _, binary_image = cv2.threshold(edges, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    return binary_image

def augment_data(image):
    datagen = ImageDataGenerator(
        rotation_range=20,
        width_shift_range=0.1,
        height_shift_range=0.1,
        shear_range=0.2,
        zoom_range=0.2,
        horizontal_flip=True,
        fill_mode='nearest'
    )

    image = np.expand_dims(image, axis=0)
    augmented_images = []

    for batch in datagen.flow(image, batch_size=1):
        augmented_images.append(batch[0].astype(np.uint8))
        if len(augmented_images) >= 5:  # 5개의 증강 이미지 생성
            break

    return augmented_images

def extract_label(filename):
    # 파일명에서 레이블 추출
    label = filename.split('_')[-1].split('.')[0]
    return label
