from picamera2 import Picamera2
import time
from datetime import datetime
import os

def setup_camera():
    """카메라 초기화 및 기본 설정"""
    picam2 = Picamera2()
    
    # 카메라 설정
    config = picam2.create_still_configuration(
        main={"size": (1920, 1080)},  # 1080p 해상도
        lores={"size": (640, 480)},   # 미리보기 해상도
        display="lores"
    )
    
    picam2.configure(config)
    return picam2

def capture_image(picam2, save_dir="captured_images"):
    """이미지 촬영 및 저장"""
    # 저장 디렉토리 생성
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)
    
    # 파일명에 현재 시간 포함
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{save_dir}/image_{timestamp}.jpg"
    
    # 이미지 촬영
    picam2.start()
    time.sleep(2)  # 카메라 안정화를 위한 대기
    picam2.capture_file(filename)
    picam2.stop()
    
    print(f"이미지가 저장되었습니다: {filename}")
    return filename

def main():
    try:
        # 카메라 초기화
        picam2 = setup_camera()
        
        # 이미지 촬영
        capture_image(picam2)
        
    except Exception as e:
        print(f"에러가 발생했습니다: {str(e)}")
    finally:
        # 카메라 정리
        picam2.close()

if __name__ == "__main__":
    main()