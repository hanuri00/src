from gpiozero import Button
from picamera2 import Picamera2, Preview
from datetime import datetime
import time

btn = Button(17)
picam2 = Picamera2()

config = picam2.create_still_configuration(main={'size':(640, 480)})
picam2.configure(config)

def capture():
    try:
        filename = f'/home/pi/zeroCar/zeroTo/img/{datetime.now():%Y-%m-%d-%H-%M-%S}.jpg'
        picam2.capture_file(filename)
        print(f'Saved as {filename}')
    except Exception as e:
        print(f"Error capturing image: {e}")

try:
    picam2.start()
    #picam2.start_preview(Preview.QTGL)
    btn.when_pressed = capture
    while True:
        time.sleep(0.1)
except KeyboardInterrupt:
    pass
finally:
    picam2.close()
    print('closed!!!1')