import cv2
import os
import numpy as np  

def preprocess_image(image_path, output_path, img224_directory):
    # 이미지 로드
    image = cv2.imread(image_path)

    # 이미지 크기 조정 (640x480)
    resized_image = cv2.resize(image, (640, 480))
    # 이미지 크기 조정 (224x224)
    resized_image224 = cv2.resize(image, (224, 224))

    # 그레이스케일로 변환
    gray_image = cv2.cvtColor(resized_image, cv2.COLOR_BGR2GRAY)

    # 가우시안 블러 적용
    blurred_image = cv2.GaussianBlur(gray_image, (5, 5), 0)

    # 이진화 처리
    _, binary_image = cv2.threshold(blurred_image, 127, 255, cv2.THRESH_BINARY)

    # 엣지 검출
    edges = cv2.Canny(blurred_image, 50, 150)

    # 이미지의 아래쪽 1/2만 선택하여 ROI 설정
    height, width = edges.shape
    roi_image = edges[int(height / 2):height, 0:width]  # 아래쪽 1/2

    # 전처리된 이미지 저장
    output_filename = os.path.join(output_path, os.path.basename(image_path))
    cv2.imwrite(output_filename, roi_image)

    # 티처블 머신 학습용 데이터 (224x224)
    img224_filename = os.path.join(img224_directory, os.path.basename(image_path))
    cv2.imwrite(img224_filename, resized_image224)  # 수정된 부분

    # 선택 사항: 전처리된 이미지 표시
    cv2.imshow('Processed Image', roi_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# 사용 예시
input_directory = 'D:\\imageData\\rawImage'  
output_directory = 'D:\\imageData\\ProcessedImage'
img224_directory = 'D:\\imageData\\img224'  
os.makedirs(output_directory, exist_ok=True)
os.makedirs(img224_directory, exist_ok=True)

# 입력 디렉토리의 모든 이미지를 처리
for filename in os.listdir(input_directory):
    if filename.endswith('.jpg'):
        preprocess_image(os.path.join(input_directory, filename), output_directory, img224_directory)
