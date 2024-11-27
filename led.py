#idk how this is gonna go but!
#this code is not mine, it's a script i found online
#goal: configure a simple LED
#current features: turns on and off in 1 second intervals

import RPi.GPIO as GPIO
from time import sleep

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(8, GPIO.OUT, initial = GPIO.LOW)

while True:
    GPIO.output(8, GPIO.HIGH)
    sleep(1)
    GPIO.output(8, GPIO.HIGH)
    sleep(1)

