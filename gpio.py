import RPi.GPIO as GPIO
import sys
import time

GPIO.setmode(GPIO.BOARD)

GPIO.setup(7, GPIO.OUT)
GPIO.setup(11, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)
t = 0.15


def blue_led():
    GPIO.output(7, GPIO.HIGH)
    print("Blue LED on!")
    time.sleep(t)
    GPIO.output(7, GPIO.LOW)

def green_led():
    GPIO.output(11, GPIO.HIGH)
    print("Green LED on!")
    time.sleep(t)
    GPIO.output(11, GPIO.LOW)

def red_led():
    GPIO.output(15, GPIO.HIGH)
    print("Red LED on!")
    time.sleep(t)
    GPIO.output(15, GPIO.LOW)

try:
    while True:
        blue_led()
        green_led()
        red_led()
        #GPIO.output(7, GPIO.HIGH)
        #print("LED is ON!")
        #time.sleep(0.5)
        #GPIO.output(7, GPIO.LOW)
        #print("LED is Out!")
        #time.sleep(0.5)
    else:                       
        GPIO.output(7, GPIO.LOW)
        GPIO.output(11, GPIO.LOW)
        GPIO.output(15, GPIO.LOW)
except KeyboardInterrupt:
    print("Programm abgebrochen...")
    GPIO.cleanup()
    sys.exit()
    
