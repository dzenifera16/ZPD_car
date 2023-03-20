import RPi.GPIO as GPIO
import os
import time
import serial

bluetooth_serial = serial.Serial("/dev/ttuS0", baudrate= 9600)
bluetooth_serial.flushInput()

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

pin1 = 3
pin2 = 5


in1 = 15
in2 = 16
in3 = 18
in4 = 22

GPIO.setup(pin1,GPIO.OUT)
GPIO.setup(pin2,GPIO.OUT)

GPIO.setup(in1,GPIO.OUT)
GPIO.setup(in2,GPIO.OUT)
GPIO.setup(in4,GPIO.OUT)
GPIO.setup(in3,GPIO.OUT)




M1_PWM = GPIO.PWM(pin1, 255)
M2_PWM = GPIO.PWM(pin2, 255)
M1_PWM.start(0)
M2_PWM.start(0)


def move_backward(velocity):
    GPIO.setmode(GPIO.BOARD)
    
    GPIO.setup(in1,GPIO.OUT)
    GPIO.setup(in2,GPIO.OUT)
    GPIO.setup(in4,GPIO.OUT)
    GPIO.setup(in3,GPIO.OUT)
            
    GPIO.output(in1,False)#forwards left wheel
    GPIO.output(in2,True)# backwards right wheel
    GPIO.output(in3,False)#forwards right wheel
    GPIO.output(in4,True)# backwards left wheel
    
    M1_PWM.ChangeDutyCycle(velocity)
    M2_PWM.ChangeDutyCycle(velocity)

    
def move_forward(velocity):
    GPIO.setmode(GPIO.BOARD)
    
    GPIO.setup(in1,GPIO.OUT)
    GPIO.setup(in2,GPIO.OUT)
    GPIO.setup(in4,GPIO.OUT)
    GPIO.setup(in3,GPIO.OUT)
#             

    GPIO.output(in1,True)#forwards left wheel
    GPIO.output(in2,False)# backwards right wheel
    GPIO.output(in3,True)#forwards right wheel
    GPIO.output(in4,False)# backwards left wheel
    
    M1_PWM.ChangeDutyCycle(velocity)
    M2_PWM.ChangeDutyCycle(velocity)
def turn_right(velocity):
    GPIO.setmode(GPIO.BOARD)
    
    GPIO.setup(in1,GPIO.OUT)
    GPIO.setup(in2,GPIO.OUT)
    GPIO.setup(in4,GPIO.OUT)
    GPIO.setup(in3,GPIO.OUT)
#             

    GPIO.output(in1,True)#forwards left wheel
    GPIO.output(in2,True)# backwards right wheel
    GPIO.output(in3,False)#forwards right wheel
    GPIO.output(in4,False)# backwards left wheel
    
    M1_PWM.ChangeDutyCycle(velocity)
    M2_PWM.ChangeDutyCycle(velocity)
    
def turn_left(velocity):
    GPIO.setmode(GPIO.BOARD)
    
    GPIO.setup(in1,GPIO.OUT)
    GPIO.setup(in2,GPIO.OUT)
    GPIO.setup(in4,GPIO.OUT)
    GPIO.setup(in3,GPIO.OUT)
#             

    GPIO.output(in1,False)#forwards left wheel
    GPIO.output(in2,False)# backwards right wheel
    GPIO.output(in3,True)#forwards right wheel
    GPIO.output(in4,True)# backwards left wheel  
def stop():
    GPIO.setmode(GPIO.BOARD)
    
    GPIO.setup(in1,GPIO.OUT)
    GPIO.setup(in2,GPIO.OUT)
    GPIO.setup(in4,GPIO.OUT)
    GPIO.setup(in3,GPIO.OUT)
    
    GPIO.output(in1,False)#forwards left wheel
    GPIO.output(in2,False)# backwards right wheel
    GPIO.output(in3,False)#forwards right wheel
    GPIO.output(in4,False)# backwards left wheel
    
    M1_PWM.ChangeDutyCycle(velocity)
    M2_PWM.ChangeDutyCycle(velocity)
    
def clean():
    GPIO.cleanup()
#     
# pump()
while True:
    
    if bluetooth_serial.in_waiting > 0:
        command = bluetooth_serial.readline().decode().strip()
    velocity = 0
    if command == 'F':
        velocity = 100
        move_forward(velocity)
    elif command == 'B':
        velocity = 100
        move_backward(velocity)
    elif command == 'L':
        velocity = 100
        turn_left(velocity)
    elif command == 'R':
        velocity = 100
        turn_right(velocity)
    elif command == 'S':
        stop()
    
    else:
        print("Invalid command")
    time.sleep(0.1)




