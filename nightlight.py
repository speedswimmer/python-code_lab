#!/usr/bin/env python3
# Python Script using PCF8591 with photoresistor and LED

import RPi.GPIO as GPIO
import time
from ADCDevice import *

ledPin = 11
adc = ADCDevice()

def setup():
    global adc
    if(adc.detectI2C(0x48)):
        adc = PCF8591()
    elif(adc.detectI2C(0x4b)):
        adc = ADS7830()
    else:
        print("No correct I2C address found")
        exit(-1)
    global p
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(ledPin, GPIO.OUT)
    GPIO.output(ledPin, GPIO.LOW)
    
    p = GPIO.PWM(ledPin,1000) #set PWM Frequence to 1kHZ
    p.start(0)
        
def loop():
    while True:
        value = adc.analogRead(0)
        p.ChangeDutyCycle(value*100/255) # Mapping the PWM duty cycle
        voltage = value / 255.0 * 3.3 # calculate the voltage value
        print("ADC Value: %d, Voltage : %.2f"%(value, voltage))
        time.sleep(0.1)

def destroy():
    adc.close()
    GPIO.cleanup()

if __name__== '__main__':
    print('Program is starting...')
    try:
        setup()
        loop()
    except KeyboardInterrupt: # Press crtl+c to end the program
        print("Program was stopped by crtl+c!")
        destroy()
