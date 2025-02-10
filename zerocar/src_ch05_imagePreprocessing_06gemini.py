import cv2
import os
import numpy as np
import json

def select_lane_lines(lines, img_shape):
    height, width = img_shape

    left_lines = []
    right_lines = []
    if lines is not None:
        for line in lines:
            x1, y1, x2, y2 = line[0]
            slope = (y2 - y1) / (x2 - x1) if (x2 - x1) != 0 else 0

            # 기울기, 위치, 길이 조건 추가
            if -0.8 < slope < -0.4 and x1 < width / 2 and x2 < width / 2 and abs(y2 - y1) > height / 4:
                left_lines.append(line)
            elif 0.4 < slope < 0.8 and x1 > width / 2 and x2 > width / 2 and abs(y2 - y1) > height / 4:
                right_lines.append(line)

    return left_lines, right_lines

def preprocess_image(image_path, output_path, img224_directory):
    try:
        image = cv2.imread(image_path)
        if image is None:
            print(f"Error: Could not read image {image_path}")
            return

        height, width, _ = image.shape

        # 1. ROI 설정 (아래쪽 1/2)
        roi_image = image[int(height / 2):height, 0:width]

        # 2. 크기 조정 (640x480 및 224x224)
        resized_image = cv2.resize(roi_image, (640, 480))
        resized_image224 = cv2.resize(image, (224, 224))

        # 3. 그레이스케일 변환
        gray_image = cv2.cvtColor(resized_image, cv2.COLOR_BGR2GRAY)

        # 4. 가우시안 블러
        blurred_image = cv2.GaussianBlur(gray_image, (5, 5), 0)

        # 5. 이진화 (Adaptive Thresholding)
        binary_image = cv2.adaptiveThreshold(blurred_image, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)

        # 6. 엣지 검출 (Canny)
        edges = cv2.Canny(binary_image, 50, 150)

        # 7. 허프 변환 (HoughLinesP)
        lines = cv2.HoughLinesP(edges, 1, np.pi / 180, 100, minLineLength=100, maxLineGap=10)

        # 8. 차선 판단
        left_lines, right_lines = select_lane_lines(lines, edges.shape)

        # 9. 차선 정보 계산 (기울기, 절편, 각도) - 수정
        lane_lines = []
        for lines_set, label in [(left_lines, "left"), (right_lines, "right")]: # 왼쪽, 오른쪽 차선에 대해 반복
            if lines_set:       # 차선이 검출된 경우에만
                for line in lines_set:
                    x1, y1, x2, y2 = line[0]
                    slope = (y2 - y1) / (x2 - x1) if (x2 - x1) != 0 else 0
                    intercept = y1 - slope * x1
                    angle = np.arctan2(y2 - y1, x2 - x1) * 180 / np.pi
                    lane_lines.append({"label": label, "x1": x1, "y1": y1, "x2": x2, "y2": y2, "slope": slope, "intercept": intercept, "angle": angle})

        # 10. 결과 저장
        output_filename = os.path.join(output_path, os.path.basename(image_path))
        cv2.imwrite(output_filename, edges)

        img224_filename = os.path.join(img224_directory, os.path.basename(image_path))
        cv2.imwrite(img224_filename, resized_image224)

        # 10. 차선 정보 JSON 파일에 저장 (수정)
        image_name = os.path.basename(image_path)
        image_data = {"image_name": image_name, "lane_lines": lane_lines}
        return image_data # JSON 데이터 반환

    except Exception as e:
        print(f"Error processing image {image_path}: {e}")
        return None

# 사용 예시
input_directory = 'D:\\imageData\\rawImage'
output_directory = 'D:\\imageData\\ProcessedImage'
img224_directory = 'D:\\imageData\\img224'
os.makedirs(output_directory, exist_ok=True)
os.makedirs(img224_directory, exist_ok=True)

all_image_data = [] # 모든 이미지 데이터를 담을 리스트

# 입력 디렉토리의 모든 이미지를 처리
for filename in os.listdir(input_directory):
    if filename.endswith('.jpg'):
        image_path = os.path.join(input_directory, filename)
        image_data = preprocess_image(image_path, output_directory, img224_directory)
        if image_data: # 이미지 데이터가 정상적으로 처리된 경우
            all_image_data.append(image_data)

# 모든 이미지 데이터를 JSON 파일에 저장 (한 번에)
json_file_path = os.path.join(output_directory, 'image_data.json')
with open(json_file_path, 'w') as f: # 'w' 모드로 파일 전체 덮어쓰기
    json.dump(all_image_data, f, indent=4) # indent 추가하여 가독성 향상

print("Preprocessing complete.")