import serial
import time
ser = serial.Serial('COM3', 9600, timeout=0)

while True:
    try:
        print(ser.readline())
        time.sleep(1)
    except ser.SerialTimeoutException:
        print('Data could not be read')
        time.sleep(1)
