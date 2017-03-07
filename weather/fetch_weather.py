#! /usr/bin/env python

# Tell your Arduino the weather forecast!

import json, requests, time
from arduino import Arduino

URL = 'http://forecast.weather.gov/MapClick.php?lat=39.173&lon=-86.5298&unit=0&lg=english&FcstType=json'
OUTPUT = '/dev/ttyACM0' # Change as needed

forecast = requests.get(URL).json()

print('{} Weather'.format(
	forecast['location']['areaDescription']))
print('Temp: {}F'.format(
	forecast['currentobservation']['Temp']))
print('Current Conditions: {}'.format(
	forecast['currentobservation']['Weather']))

board = Arduino(OUTPUT)
pin = 13

board.output([pin])

# Blink the LED as many times as the current temp
for x in range(1, int(forecast['currentobservation']['Temp'])):
	board.setHigh(pin)
	time.sleep(0.2)
	board.setLow(pin)
	time.sleep(0.2)

board.close()
