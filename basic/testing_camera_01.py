from picamera2 import Picamera2

cam = Picamera2()

cam.start()

cam.capture_file('test.jpg')

cam.close()
