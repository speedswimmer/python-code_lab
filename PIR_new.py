import RPi.GPIO as GPIO
import time, sys
import picamera
import os
from os import path
import ftplib

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(7, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

def logentry(entry):
    #Check if Logfile exists and open it accordingly or create a new file
    if path.exists('/home/pi/Pictures/PIR/log.txt') == True:
        f=open('/home/pi/Pictues/PIR/log.txt', 'a')
    else:
        f=open('/home/pi/Pictures/PIR/log.txt', 'w+')
    f.write(entry)
    f.close

#Pin for LED
GPIO.setup(11, GPIO.OUT)

#f=open("/home/pi/Pictures/PIR/logfile.txt", "w+")

cam = picamera.PiCamera()
cam.resolution = (1080,768)

def pic():
    t=time.strftime('%Y_%m_%d-%H:%M:%S')
    filename = ('bild_%s.jpg' %t)
    cam.capture('/home/pi/Pictures/PIR/bild_%s.jpg' %t)
    logentry(filename)
   
def actual_time():
    tstamp = time.strftime("%H:%M:%S")
    return tstamp

def led():
    GPIO.output(11, GPIO.HIGH)
    print("LED on!")
    time.sleep(t)
    GPIO.output(11, GPIO.LOW)

def motion(pin):
    tstamp = time.strftime("%H.%M.%S")
    print("Achtung! Bewegung erkannt - " + actual_time())
    led()
    pic()
    return

#Program Start
actual_time()
t=0.5
print('Überwachung gestartet...' + actual_time())
led()
t=0.2

#deactivate display
os.system("vcgencmd display_power 0") 

GPIO.add_event_detect(7, GPIO.RISING)
GPIO.add_event_callback(7, motion)

try:
    while True:
        time.sleep(t)
except KeyboardInterrupt:
    os.system("vcgencmd display_power 1") 
    print('Programm abgebrochen!')
    GPIO.cleanup()
    sys.exit()
        
