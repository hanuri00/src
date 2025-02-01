#! /usr/bin/env python

import drivers
from time import sleep

dp = drivers.Lcd()


while True:
    print('Writing to display')
    dp.lcd_display_string('Go....!', 1)
    dp.lcd_display_string('Stop..!', 2)
    sleep(2)
    dp.lcd_clear()
    sleep(2)
