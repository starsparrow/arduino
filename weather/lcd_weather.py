#!/usr/bin/env python

import time
import serial
import requests

FORECAST_URL = 'http://forecast.weather.gov/MapClick.php?lat=39.1653&lon=-86.5264&unit=0&lg=english&FcstType=json'

data = requests.get(FORECAST_URL).json()['currentobservation']
line1 = 'Currently: {}F{}'.format(data['Temp'], ' ' * (4 - len(str(data['Temp']))))
line2 = '{}'.format(data['Weather'])
msg = str.encode('{}{}'.format(line1, line2))

ser = serial.Serial('COM3', 9600, timeout=0)
time.sleep(2.5)  # Wait for serial connection to be established
ser.write(msg)
ser.close()
