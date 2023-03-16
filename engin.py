import RPi.GPIO as GPIO
import os
import time
import serial




GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

# pin1 = 3
# pin2 = 5


in1 = 15
in2 = 16
in3 = 18
in4 = 22

# GPIO.setup(pin1,GPIO.OUT)
# GPIO.setup(pin2,GPIO.OUT)

GPIO.setup(in1,GPIO.OUT)
GPIO.setup(in2,GPIO.OUT)
GPIO.setup(in4,GPIO.OUT)
GPIO.setup(in3,GPIO.OUT)

# GPIO.output(in1,True)#forwards left wheel
# GPIO.output(in2,False)# backwards right wheel
# GPIO.output(in3,True)#forwards right wheel
# GPIO.output(in4,False)# backwards left wheel
# 



# 
time.sleep(5)
GPIO.cleanup()
# 
# # def pump():
#     GPIO.output(pin2, GPIO.HIGH)
#     print ("pump running")
#     GPIO.output(pin1, GPIO.HIGH)
def backwards():
    GPIO.setmode(GPIO.BOARD)
    
    GPIO.setup(in1,GPIO.OUT)
    GPIO.setup(in2,GPIO.OUT)
    GPIO.setup(in4,GPIO.OUT)
    GPIO.setup(in3,GPIO.OUT)
            
    GPIO.output(in1,False)#forwards left wheel
    GPIO.output(in2,True)# backwards right wheel
    GPIO.output(in3,False)#forwards right wheel
    GPIO.output(in4,True)# backwards left wheel

    time.sleep(0.5)
def forwards():
    GPIO.setmode(GPIO.BOARD)
    
    GPIO.setup(in1,GPIO.OUT)
    GPIO.setup(in2,GPIO.OUT)
    GPIO.setup(in4,GPIO.OUT)
    GPIO.setup(in3,GPIO.OUT)
            

    GPIO.output(in1,True)#forwards left wheel
    GPIO.output(in2,False)# backwards right wheel
    GPIO.output(in3,True)#forwards right wheel
    GPIO.output(in4,False)# backwards left wheel
    time.sleep(0.5)
def forwards():
    GPIO.setmode(GPIO.BOARD)
    
    GPIO.setup(in1,GPIO.OUT)
    GPIO.setup(in2,GPIO.OUT)
    GPIO.setup(in4,GPIO.OUT)
    GPIO.setup(in3,GPIO.OUT)
            

    GPIO.output(in1,True)#forwards left wheel
    GPIO.output(in2,False)# backwards right wheel
    GPIO.output(in3,True)#forwards right wheel
    GPIO.output(in4,False)# backwards left wheel
    time.sleep(0.5)
    
def clean():
    GPIO.cleanup()
#     
# pump()
backwards()
forwards()
clean()

