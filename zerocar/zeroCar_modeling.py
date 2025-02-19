# -*- coding: utf-8 -*-
# update : {current_date}
# author : hanuri00
# description : zeroCar Project - Modeling
# zeroCar_modeling.py

import os
import numpy as np
import cv2
from keras import layers, models
from zeroCar_preprocess_image import preprocess_image, extract_label  # 전처리 함수 가져오기

def unet_model(input_size=(256, 256, 1)):
    inputs = layers.Input(input_size)

    # U-Net 아키텍처 정의
    c1 = layers.Conv2D(64, (3, 3), activation='relu', padding='same')(inputs)
    c1 = layers.Conv2D(64, (3, 3), activation='relu', padding='same')(c1)
    p1 = layers.MaxPooling2D((2, 2))(c1)

    c2 = layers.Conv2D(128, (3, 3), activation='relu', padding='same')(p1)
    c2 = layers.Conv2D(128, (3, 3), activation='relu', padding='same')(c2)
    p2 = layers.MaxPooling2D((2, 2))(c2)

    c3 = layers.Conv2D(256, (3, 3), activation='relu', padding='same')(p2)
    c3 = layers.Conv2D(256, (3, 3), activation='relu', padding='same')(c3)
    p3 = layers.MaxPooling2D((2, 2))(c3)

    c4 = layers.Conv2D(512, (3, 3), activation='relu', padding='same')(p3)
    c4 = layers.Conv2D(512, (3, 3), activation='relu', padding='same')(c4)
    p4 = layers.MaxPooling2D((2, 2))(c4)

    c5 = layers.Conv2D(1024, (3, 3), activation='relu', padding='same')(p4)
    c5 = layers.Conv2D(1024, (3, 3), activation='relu', padding='same')(c5)

    # 업샘플링 경로
    u6 = layers.Conv2DTranspose(512, (2, 2), strides=(2, 2), padding='same')(c5)
    u6 = layers.concatenate([u6, c4])
    c6 = layers.Conv2D(512, (3, 3), activation='relu', padding='same')(u6)
    c6 = layers.Conv2D(512, (3, 3), activation='relu', padding='same')(c6)

    u7 = layers.Conv2DTranspose(256, (2, 2), strides=(2, 2), padding='same')(c6)
    u7 = layers.concatenate([u7, c3])
    c7 = layers.Conv2D(256, (3, 3), activation='relu', padding='same')(u7)
    c7 = layers.Conv2D(256, (3, 3), activation='relu', padding='same')(c7)

    u8 = layers.Conv2DTranspose(128, (2, 2), strides=(2, 2), padding='same')(c7)
    u8 = layers.concatenate([u8, c2])
    c8 = layers.Conv2D(128, (3, 3), activation='relu', padding='same')(u8)
    c8 = layers.Conv2D(128, (3, 3), activation='relu', padding='same')(c8)

    u9 = layers.Conv2DTranspose(64, (2, 2), strides=(2, 2), padding='same')(c8)
    u9 = layers.concatenate([u9, c1])
    c9 = layers.Conv2D(64, (3, 3), activation='relu', padding='same')(u9)
    c9 = layers.Conv2D(64, (3, 3), activation='relu', padding='same')(c9)

    outputs = layers.Conv2D(1, (1, 1), activation='sigmoid')(c9)
    model = models.Model(inputs=[inputs], outputs=[outputs])
    return model

if __name__ == "__main__":
    image_folder = "d:/preprocess_image/"  # 이미지 폴더 경로
    mask_folder = "d:/masks/"  # 마스크 폴더 경로

    images = []
    masks = []

    for filename in os.listdir(image_folder):
        if filename.endswith(".jpg") or filename.endswith(".png"):
            image_path = os.path.join(image_folder, filename)

            # 레이블 추출
            action = extract_label(filename)

            # 전처리
            preprocessed_image = preprocess_image(image_path)
            images.append(preprocessed_image)

            # 마스크 로드 및 전처리
            mask_path = os.path.join(mask_folder, filename)  # 마스크 경로
            mask = cv2.imread(mask_path, cv2.IMREAD_GRAYSCALE)
            masks.append(mask)

    # numpy 배열로 변환
    X = np.array(images)
    y = np.array(masks)

    # 이미지 차원 조정
    X = np.expand_dims(X, axis=-1)  # (height, width) -> (height, width, 1)
    y = np.expand_dims(y, axis=-1)  # (height, width) -> (height, width, 1)

    # U-Net 모델 생성
    model = unet_model(input_size=(X.shape[1], X.shape[2], 1))
    model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

    # 모델 학습
    model.fit(X, y, validation_split=0.1, epochs=50, batch_size=16)

    # 모델 저장
    model.save('lane_detection_model.h5')
