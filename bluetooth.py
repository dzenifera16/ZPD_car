# from machine import *
# import serial
# uart = UART(0,9600)
# 
# while True:
#     # print('checking BT')
#     if uart.any():
#         command = uart.readline()
#         print(command)
#         
import serial
from time import sleep
ser = serial.Serial ("/dev/ttyAMA0", 9600) 
while True:
    received_data = ser.read()              #read serial port
    sleep(0.03)
    data_left = ser.inWaiting()             #check for remaining byte
    received_data += ser.read(data_left)
    print (received_data)                   #print received data
    ser.write(received_data)
# wiringpi.wiringPiSetup()
# ser = wiringpi.serialOpen("/dev/ttyAMA0", 9600)
# wiringpi.serialPuts(ser, 'hello wworld')


# ser = serial.Serial ("/dev/ttyAMA0", 115200)    #Open port with baud rate


#
# while True:
#     received_data = ser.read()              #read serial port
#     sleep(0.03)
#     data_left = ser.inWaiting()             #check for remaining byte
#     received_data += ser.read(data_left)
#     print (received_data)                   #print received data
#     ser.write(received_data)
# import serial
# ser = serial.Serial('/dev/ttyAMA0', timeout=1, baudrate=9600)
# serial.flushInput();serial.flushOutput()
#    
# while True:
#     out = serial.readline().decode()
#     if out!='' : print (out)
#     if out == 'exit': break