import RPi.GPIO as GPIO
import os
import time
import serial




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
    command = input("Enter a command: ")
    velocity = 0
    if command == 'f':
        velocity = 100
        move_forward(velocity)
    elif command == 'b':
        velocity = 100
        move_backward(velocity)
    elif command == 'l':
        velocity = 100
        turn_left(velocity)
    elif command == 'r':
        velocity = 100
        turn_right(velocity)
    elif command == 's':
        stop()
    
    else:
        print("Invalid command")
    time.sleep(0.1)

# 
# import RPi.GPIO as GPIO
# import time
# 
# GPIO.setwarnings(False)
# GPIO.setmode(GPIO.BCM)
# # Set the GPIO pins for the left motor
# in1 = 15
# in4 = 22
# pin2 = 5
# 
# 
# 
# # Set the GPIO pins for the right motor
# in2 = 16
# in3 = 18
# pin1 = 3
# 
# 
# # Set up the GPIO pins
# 
# GPIO.setup(pin1,GPIO.OUT)
# GPIO.setup(pin2,GPIO.OUT)
# 
# GPIO.setup(in1,GPIO.OUT)
# GPIO.setup(in2,GPIO.OUT)
# GPIO.setup(in4,GPIO.OUT)
# GPIO.setup(in3,GPIO.OUT)
# 
# # # Set the PWM for the motor enable pins
# M1_PWM = GPIO.PWM(pin1, 100)
# M2_PWM = GPIO.PWM(pin2, 100)
# M1_PWM.start(0)
# M2_PWM.start(0)
# 
# def move_forward():
#     GPIO.setup(pin1,GPIO.OUT)
#     GPIO.setup(pin2,GPIO.OUT)
#     
#     GPIO.setup(in1,GPIO.OUT)
#     GPIO.setup(in2,GPIO.OUT)
#     GPIO.setup(in4,GPIO.OUT)
#     GPIO.setup(in3,GPIO.OUT)
#     
#     GPIO.output(in1,True)#forwards left wheel
#     GPIO.output(in2,False)# backwards right wheel
#     GPIO.output(in3,True)#forwards right wheel
#     GPIO.output(in4,False)# backwards left wheel
#     time.sleep(0.5)
#   
#     M1_PWM.ChangeDutyCycle(velocity)
#     M2_PWM.ChangeDutyCycle(velocity)
# 
# def move_backward(velocity):
#     GPIO.setup(pin1,GPIO.OUT)
#     GPIO.setup(pin2,GPIO.OUT)
#     GPIO.output(in1,True)#forwards left wheel
#     GPIO.output(in2,False)# backwards right wheel
#     GPIO.output(in3,True)#forwards right wheel
#     GPIO.output(in4,False)# backwards left wheel
#     time.sleep(0.5)
#     M1_PWM.ChangeDutyCycle(velocity)
#     M2_PWM.ChangeDutyCycle(velocity)
# 
# def turn_left(velocity):
#     
#     GPIO.output(in1,False)#forwards left wheel
#     GPIO.output(in2,False)# backwards right wheel
#     GPIO.output(in3,True)#forwards right wheel
#     GPIO.output(in4,True)# backwards left wheel
#     M1_PWM.ChangeDutyCycle(velocity)
#     M2_PWM.ChangeDutyCycle(velocity)
# 
# def turn_right(velocity):
#     GPIO.output(in1,True)#forwards left wheel
#     GPIO.output(in2,True)# backwards right wheel
#     GPIO.output(in3,False)#forwards right wheel
#     GPIO.output(in4,False)# backwards left wheel
#     M1_PWM.ChangeDutyCycle(velocity)
#     M2_PWM.ChangeDutyCycle(velocity)
# 
# def stop():
#     GPIO.output(in1,False)#forwards left wheel
#     GPIO.output(in2,False)# backwards right wheel
#     GPIO.output(in3,False)#forwards right wheel
#     GPIO.output(in4,False)# backwards left wheel
#     M1_PWM.ChangeDutyCycle(0)
#     M2_PWM.ChangeDutyCycle(0)
# def clean():
#     GPIO.cleanup()
# while True:
#     command = input("Enter a command: ")
#     velocity = 0
#     if command == 'f':
#         velocity = 100
#         move_forward(velocity)
#     elif command == 'b':
#         velocity = 50
#         move_backward(velocity)
#     elif command == 'l':
#         velocity = 50
#         turn_left(velocity)
#     elif command == 'r':
#         velocity = 50
#         turn_right(velocity)
#     elif command == 's':
#         stop()
#     
#     else:
#         print("Invalid command")
#     time.sleep(0.1)

            



