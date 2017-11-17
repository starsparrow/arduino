#!/usr/bin/env/ python

import sys
import time
import serial
import sqlalchemy

ser = serial.Serial('COM3', 9600, timeout=0)

username = ''
password = ''
server = ''
database = ''
query = ''

conn = 'mssql+pymssql://{}:{}@{}/{}'.format(username, password, server, database)
engine = sqlalchemy.create_engine(conn)

items = []
for row in engine.execute(query):
    items.append('{} {}'.format(row.col1, row.col2))  # change col1 and col2, add more, etc.

while True:
    for item in items:
        ser.write(str.encode(item))
        time.sleep(0.5)
        
