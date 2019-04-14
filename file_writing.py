import os
from os import path
import datetime
from datetime import date, time, timedelta
import time

if path.exists("text.txt") == True:
    print(str(path.exists("text.txt")))
    print("Datei existiert!")
else:
    print("Datei nicht vorhanden")

f = open("text.txt", "r")

#for i in range(10):
#    f.write("This is line "+ str(i) + "\r\n")
#    f.close

if f.mode == 'r':
    contents = f.read()
    print(contents)
else:
    print("Nichts")
    

