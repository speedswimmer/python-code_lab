#!/usr/bin/env python3
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

trig = 11
echo = 13
red_led = 26
blue_led = 32
green_led = 36

GPIO.setup(echo, GPIO.IN)
GPIO.setup(trig, GPIO.OUT)
GPIO.setup(red_led, GPIO.OUT)
GPIO.setup(blue_led, GPIO.OUT)
GPIO.setup(green_led, GPIO.OUT)

while True:
    GPIO.output(trig, True)
    time.sleep(0.00001)
    GPIO.output(trig, False)
    
    while GPIO.input(echo) == 0:
        pass
    start = time.time()
    
    while GPIO.input(echo) == 1:
        pass
    ende = time.time()
    
    entfernung = ((ende - start) * 34300) / 2
    
    if entfernung >=100:
        GPIO.output(red_led, GPIO.LOW)
        GPIO.output(blue_led, GPIO.LOW)
        GPIO.output(green_led, GPIO.LOW)
        
    else:
        print(f"Entfernung: {entfernung:.3} cm")
        
        if entfernung <=13:
            GPIO.output(red_led, GPIO.HIGH)
            GPIO.output(blue_led, GPIO.LOW)
            GPIO.output(green_led, GPIO.LOW)
        elif entfernung <=30:
            GPIO.output(blue_led, GPIO.HIGH)
            GPIO.output(red_led, GPIO.LOW)
            GPIO.output(green_led, GPIO.LOW)
        elif entfernung <=60:
            GPIO.output(green_led, GPIO.HIGH)
            GPIO.output(red_led, GPIO.LOW)
            GPIO.output(blue_led, GPIO.LOW)

    time.sleep(0.3)

