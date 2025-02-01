from picamera2 import Picamera2, Preview
from time import sleep

cam = Picamera2()

video_file = "output.h264"

cam.start_preview(Preview.QTGL)

cam.start_recording(video_file)

sleep(5)

cam.stop_recording()

cam.stop_preview()