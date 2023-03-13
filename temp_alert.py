#!/usr/bin/env python3

import time
import smbus2
import bme280
import signal
import sys
from messaging import send_email

def handle_keyboard_interrupt(signal, frame):
        print('nKeyboard interrupt detected, stopping the scripts...')
        sys.exit(0)

signal.signal(signal.SIGINT, handle_keyboard_interrupt)

LOG_FILE = "/home/pi/Scripts/bme280.txt"

# create an instance of the BME280 Sensor
bus = smbus2.SMBus(1)

# initialize the BME280 sensor
address = 0x76
calibration_params = bme280.load_calibration_params(bus, address)

# Set up variables to track the highest and lowest temperature
highest_temp = None
lowest_temp = None
high_time = None
low_time = None

# Loop forever
while True:
        bme280data = bme280.sample(bus, address, calibration_params)
        temp = bme280data.temperature
        humidity = bme280data.humidity
        pressure = bme280data.pressure

        # Check if this is the first loop iteration, or if it's been more than
        # 3 hours since the last temperature measurement.
        if highest_temp is None or time.monotonic() - high_time >= 14400:
                highest_temp = temp
                lowest_temp = temp
                high_time = time.monotonic()
                low_time = time.monotonic()

        else:
        # Check if the current temperature is higher than the highest temperature.
                if temp > highest_temp:
                        highest_temp = temp
                        high_time = time.monotonic()

                elif temp < lowest_temp:
                        lowest_temp = temp
                        low_time = time.monotonic()
        # calculate the temperature change between highest and lowest temperature
        temp_range = highest_temp - lowest_temp

        if temp_range >=3:
                                with open(LOG_FILE, "a") as f:
                                        timestamp = time.strftime("%d.%m.%y - %H:%M")
                                        f.write(f'{timestamp} - ALERT! Temperature dropped by more than 3°C within last 4 hours!\n')
                                send_email('ALERT - Temperature has dropped by more than 3°C within last 4 hours!')

                                # Update the highest and lowest temperature available
                                highest_temp = temp
                                lowest_temp = temp
                                high_time = time.monotonic()
                                low_time = time.monotonic()

        # Wait for 30 minutes before taking the next measurement
        with open(LOG_FILE, "a") as b:
                b.write(f'{time.strftime("%d.%m.%y - %H:%M")} | ')
                b.write(f'Humidity: {humidity:.1f}% ; ')
                b.write(f'Pressure: {pressure:.1f} hPa ; ')
                b.write(f'Hi-Temp = {highest_temp:.2f} °C ; ')
                b.write(f'Lo-Temp = {lowest_temp:.2f} °C ; ')
                b.write(f'Current Temp = {temp:.2f} °C\n')
        time.sleep(1800)
