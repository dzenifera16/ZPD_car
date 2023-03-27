import RPi.GPIO as GPIO
import os
import time
import serial

# bluetooth_serial = serial.Serial("/dev/ttuS0", baudrate= 9600)
# bluetooth_serial.flushInput()

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

channel = 16
GPIO.setup(channel, GPIO.IN)

M1_PWM = GPIO.PWM(pin1, 255)
M2_PWM = GPIO.PWM(pin2, 255)
M1_PWM.start(0)
M2_PWM.start(0)


def callback(channel):
    if GPIO.input(channel):
        print('sound detected')

    else: 
        print('sound detected')

GPIO.add_event_detect(channel, GPIO.BOTH, bouncetime=100)
GPIO.add_event_callback(channel, callback)

def distance():
       PIN_TRIGGER = 7
       PIN_ECHO = 11
        
       GPIO.setmode(GPIO.BOARD)

       GPIO.setup(PIN_TRIGGER, GPIO.OUT)
       GPIO.setup(PIN_ECHO, GPIO.IN)
       
       
       
   
 
       GPIO.output(PIN_TRIGGER, GPIO.LOW)
 
#        print ("Waiting for sensor to settle")
 
       time.sleep(0.00001)
 
#        print ("Calculating distance")

       GPIO.output(PIN_TRIGGER, GPIO.HIGH)
       
       startTime = time.time()
       arrivalTime = time.time()

       time.sleep(0.0001)
 
       GPIO.output(PIN_TRIGGER, GPIO.LOW)
 
       while GPIO.input(PIN_ECHO)==0:
             startTime = time.time()
       while GPIO.input(PIN_ECHO)==1:
             arrivalTime = time.time()
       duration = arrivalTime - startTime
       distance = round((duration * 34300)/ 2)
       return distance
    
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
    distance2 = distance()
    sound= callback(channel)
    print(sound)
    command= input("Ievadi komandu: ")
#     if bluetooth_serial.in_waiting > 0:
#         command = bluetooth_serial.readline().decode().strip()
    velocity = 0
    
    if command == 'F' :
        velocity = 100
        move_forward(velocity)
        print(distance2)
        if distance2 > 30:
            move_forward(velocity)
            
        else:
            stop()
            
            
    elif command == 'B':
        velocity = 100
        move_backward(velocity)
    elif command == 'L':
        velocity = 100
        turn_left(velocity)
    elif command == 'R':
        velocity = 100
        turn_right(velocity)
    elif command == 'S' :
        stop()

    
    else:
        print("par tuvu")
    time.sleep(0.1)




