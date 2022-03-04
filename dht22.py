import Adafruit_DHT
import time
from datetime import datetime

sensor = Adafruit_DHT.DHT22
pin = 12

print("[press ctrl+c to stop the script]...")

try:
        while True:
                now = datetime.now()
                timestamp = now.strftime('%d.%m.%Y %H:%M')
                humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
                if humidity is not None and temperature is not None:
                        print(timestamp, "Temp={0:0.1f}°C, Humidity={1:0.1f}%".format(temperature, humidity))
                else:
                        print("Failed to get reading. Try again!")
                time.sleep(60)
except KeyboardInterrupt:
        print("Script stopped!")
