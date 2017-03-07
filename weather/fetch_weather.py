#! /usr/bin/env python

import json, requests

url = 'http://forecast.weather.gov/MapClick.php?lat=39.173&lon=-86.5298&unit=0&lg=english&FcstType=json'

forecast = requests.get(url).json()

print('{} Weather'.format(
	forecast['location']['areaDescription']))
print('Temp: {}F'.format(
	forecast['currentobservation']['Temp']))
print('Current Conditions: {}'.format(
	forecast['currentobservation']['Weather']))