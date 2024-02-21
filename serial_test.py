import serial_test
from time import sleep

ser = serial_test.Serial("/dev/ttyS0", 9600)    #Open port with baud rate
while True:
    received_data = ser.read()
    sleep(0.03)
    data_left = ser.inWaiting()
    received_data += ser.read(data_left)
    print(received_data)
    ser.write(received_data)