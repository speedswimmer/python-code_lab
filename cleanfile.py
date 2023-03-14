#!/usr/bin/env python3
import sys
import signal

def handle_keyboard_interrupt(signal, frame):
        print('\nKeyboard interrupt detected, stopping the script...')
        sys.exit(0)

signal.signal(signal.SIGINT, handle_keyboard_interrupt)


try:
        with open ('/home/pi/Scripts/bme280.txt', 'r') as f:
                lines = f.readlines()
                linecount = len(lines)
                print(f'Die Datei enthält {linecount} Zeilen!')

except Exception as err:
        print(f'Unexpected {err=}')
        sys.exit(0)

except OSError as err:
        print("OS error:", err)

try:
        a = int(input('Wie viele Zeilen sollen vom Anfang gelöscht werden (ganze Zahl, 0 für keine)? '))

        if a == 0:
                print('No line will be deleted!')
                sys.exit(0)
        elif a>0 and a<= linecount:
                with open('/home/pi/Scripts/bme280.txt', 'r+') as fp:
                        lines = fp.readlines()
                        fp.seek(0)
                        fp.truncate()
                        fp.writelines(lines[a:])

        else:
                print('No valid entry, script stopped!')

except:
        print('No valid entry!')

finally:
        sys.exit(0)
