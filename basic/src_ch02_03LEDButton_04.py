from gpiozero import LED, Button
from time import sleep

led1 = LED(17)
led2 = LED(27)
led3 = LED(22)

btn1 = Button(16)
btn2 = Button(20)
btn3 = Button(21)

while True:
    led1.source=btn1
    led2.source=btn2
    led3.source=btn3
    sleep(1)
