import serial
import time

DataSerial = serial.Serial('COM3' , 115200)

while True:
    while DataSerial.in_waiting == 0:
        pass

    data = DataSerial.readline()
    data = str(data, encoding='utf-8')
    data = data.strip('\r\n')

    data = data.split(',')
    print(data)

    x = float(data[0])
    y = float(data[1])
    z = float(data[2])

    print('x = ' , x , 'y = ' , y , 'z = ' , z)