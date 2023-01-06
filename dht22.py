#!/usr/bin/env python3
import Adafruit_DHT
import time
from datetime import datetime
import json

sensor = Adafruit_DHT.DHT22
pin = 23
interval = 1800

print("[press ctrl+c to stop the script]...")

try:
        while True:
                now = datetime.now()
                env_data = {}
                entry = {}
                timestamp = now.strftime('%d.%m.%Y %H:%M')
                humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
                if humidity is not None and temperature is not None:
                        env_data["Temp"]=round(temperature, 1)
                        env_data["Hum"]=round(humidity, 1)
                        entry[timestamp]=env_data
                        print(timestamp, "Temp={0:0.1f}°C, Humidity={1:0.1f}%".format(temperature, humidity))
                        with open ("environment.json", "a") as f:
                                json.dump(entry, f)
                else:
                        print("Failed to get reading. Try again!")
                time.sleep(interval)

except KeyboardInterrupt:
        print("[...script stopped!]")
