import RPi.GPIO as GPIO
import os

GPIO.cleanup()
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

pin1 = 2
pin2 = 3

in1 = 4
in2 = 17
in3 = 27
in4 = 22

GPIO.setup(pin1,GPIO.OUT)
GPIO.setup(pin2,GPIO.OUT)

GPIO.setup(in1,GPIO.OUT)
GPIO.setup(in2,GPIO.OUT)
GPIO.setup(in4,GPIO.OUT)
GPIO.setup(in3,GPIO.OUT)

def pump():
    GPIO.output(pin2, GPIO.HIGH)
    print ("pump running")
    GPIO.output(pin1, GPIO.HIGH)
def backwards():
    GPIO.output(in1, GPIO.HIGH)
    GPIO.output(in4, GPIO.HIGH)
    print ("backwards running")
    GPIO.output(in2, GPIO.LOW)
    GPIO.output(in3, GPIO.LOW)
def clean():
    GPIO.cleanup()
    
pump()
backwards()
clean()
