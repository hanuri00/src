from picamera2 import Picamera2, Preview
from time import sleep, time
from datetime import datetime
import os

picam2 = Picamera2()

config = picam2.create_still_configuration(main={'size': (640, 480)})
picam2.configure(config)

picam2.start_preview(Preview.QTGL)

picam2.start()
sleep(2)

try:
    while True:
        start_time = time()
        now = datetime.now()
        timestamp = now.strftime("%Y-%m-%d-%H-%M-%S")

        # 저장 디렉토리 경로
        save_dir = "/home/pi/zeroCar/zeroTo/img"

        # 디렉토리가 존재하지 않으면 생성
        if not os.path.exists(save_dir):
            os.makedirs(save_dir)

        filename = os.path.join(save_dir, f"image_{timestamp}.jpg") # 파일 경로 생성
        picam2.capture_file(filename)
        print(f"Captured {filename}")
        elapsed_time = time() - start_time
        sleep(max(0, 5 - elapsed_time))

except KeyboardInterrupt:
    print("Stopped by user")

finally:
    picam2.close()
    print("Camera closed")