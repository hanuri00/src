# -*- coding: utf-8 -*-

from picamera2 import Picamera2, Preview
from time import sleep

picam2 = Picamera2()

config = picam2.create_still_configuration(
    main={
        'size':(640, 480)
    }
)
picam2.configure(config)

picam2.start_preview(Preview.QTGL)

picam2.start()
sleep(5)

picam2.capture_file("test.jpg")

picam2.close()

print('Saved as test.jpg ')