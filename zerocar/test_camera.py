from picamera2 import Picamera2

cam = Picamera2()

cam.start()

cam.capture_file('/home/pi/zeroCar/src/imgtest.jpg')

cam.close()