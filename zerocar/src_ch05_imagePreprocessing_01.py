# notebook... 
# workday : 20250204

import cv2
import numpy as np
import os
import json

def preprocess_image(image_path):
    """
    차선 이미지를 전처리합니다.

    Args:
        image_path (str): 차선 이미지 경로

    Returns:
        numpy.ndarray: 전처리된 이미지
        dict: 차선 정보 (위치, 각도 등)
    """

    # 1. 이미지 로드
    img = cv2.imread(image_path)
    height, width, _ = img.shape

    # 2. ROI 설정 (이미지 아래쪽 1/2)
    new_height = int(height / 2)
    resized_img = img[new_height:height, 0:width]

    # 3. 색상 공간 변환 (HSV)
    hsv = cv2.cvtColor(resized_img, cv2.COLOR_BGR2HSV)

    # 4. 특정 색상 범위 마스크 생성 (흰색 차선 검출)
    lower_white = np.array([0, 0, 200])  # 낮은 채도, 높은 명도
    upper_white = np.array([180, 20, 255]) # 최대 채도, 최대 명도
    mask = cv2.inRange(hsv, lower_white, upper_white)

    # 5. 마스크를 이용하여 원본 이미지에서 흰색 차선 추출
    white_lines = cv2.bitwise_and(resized_img, resized_img, mask=mask)

    # 6. 엣지 검출 (Canny)
    gray = cv2.cvtColor(white_lines, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 50, 150, apertureSize=3)

    # 7. 허프 변환 (HoughLinesP) - 직선 검출
    lines = cv2.HoughLinesP(edges, 1, np.pi / 180, 100, minLineLength=100, maxLineGap=10)

    # 8. 차선 정보 계산 (기울기, 절편)
    lane_lines = []
    if lines is not None:
        for line in lines:
            x1, y1, x2, y2 = line[0]
            slope = (y2 - y1) / (x2 - x1) if (x2 - x1) != 0 else 0  # 기울기 계산
            intercept = y1 - slope * x1  # 절편 계산
            angle = np.arctan2(y2 - y1, x2 - x1) * 180 / np.pi  # 각도 계산
            lane_lines.append({"x1": x1, "y1": y1, "x2": x2, "y2": y2, "slope": slope, "intercept": intercept, "angle": angle})

    # 9. 결과 이미지 저장
    #cv2.imwrite("preprocessed_image.jpg", edges)

    # 11. 차선 정보 반환
    return edges, lane_lines

# 이미지 파일 경로 목록
image_dir = "path/to/your/image/directory" # 이미지 파일이 있는 디렉토리 경로 설정
image_files = [os.path.join(image_dir, f) for f in os.listdir(image_dir) if f.endswith(".jpg")]

# 각 이미지에 대해 전처리 수행
for image_file in image_files:
    preprocessed_image, lane_lines = preprocess_image(image_file)

    # 차선 정보 JSON 파일에 저장
    image_name = os.path.basename(image_file)
    data = {"image_name": image_name, "lane_lines": lane_lines}

    json_file_path = os.path.join(image_dir, 'image_data.json')
    with open(json_file_path, 'a') as f:
        json.dump(data, f)
        f.write('\n')

    print(f"Processed: {image_file}")