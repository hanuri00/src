# -*- coding: utf-8 -*-

from picamera2 import Picamera2, controls
from time import sleep
import os
from datetime import datetime

picam2 = Picamera2()

# ������ ���� ��� ���� �� ���丮 ����
save_dir = "/home/pi/zeroCar/zeroTo/video"
os.makedirs(save_dir, exist_ok=True) # exist_ok=True �߰�

try:
    while True:
        now = datetime.now()
        timestamp = now.strftime("%Y-%m-%d-%H-%M-%S")
        filename = os.path.join(save_dir, f"vid_{timestamp}.mp4")

        # ������ ���� (������) - �ػ�, ������ ����Ʈ ���� ������ �� �ֽ��ϴ�.
        video_config = picam2.create_video_configuration(main={"size": (640, 480)})
        picam2.configure(video_config)
        picam2.start_recording(filename)
        print(f"Recording started: {filename}")
        sleep(5)
        picam2.stop_recording()
        print(f"Recording stopped: {filename}")
        sleep(1)

except KeyboardInterrupt:
    print("Keyboard Interruptted")
except Exception as err:
    print(f"Error : {err}")
finally:
    picam2.close()
    print("Programming finished")