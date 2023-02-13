#!/usr/bin/python
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

GPIO.setup(PIN_TRIGGER, GPIO.OUT)
GPIO.setup(PIN_ECHO, GPIO.IN)
def distance():
       
       
       PIN_TRIGGER = 7
       PIN_ECHO = 11
   
 
       GPIO.output(PIN_TRIGGER, GPIO.LOW)
 
       print ("Waiting for sensor to settle")
 
       time.sleep(0.00001)
 
       print ("Calculating distance")

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
  
if __name__ == '__main__':
    try:
        while True:
            distance = distance()
            print ("Measured distance = %.1f cm" % distance)
            time.sleep(1) #
        
    except KeyboardInterrupt:
        print("Measurement stopped by user")
        GPIO.cleanup()
#             if distance > 20:
#              pulse_duration = pulse_end_time - pulse_start_time
#              distance = round(duration * 17150, 2)
#              print ("Distance:",distance,"cm")
#              
#          else:
#              print('par tuvu')
       
             


# 
# 
# import RPi.GPIO as g
# import time as t
# g.setmode(g.BCM)
# g.setwarnings(False)
# 
# # trig is the pin on the sensor which will emit a very fast pulse
# trig = 7
# # echo is the pin which will recieve the pulse from the trig 
# echo = 11
# 
# g.setup(trig, g.OUT)
# g.setup(echo, g.IN)
# 
# def distance(dur):
#     global dis
#     start = 0
#     end = 0
#     g.output(trig, g.LOW)
#     t.sleep(0.01)
#     g.output(trig, g.HIGH)
#     t.sleep(0.00001)
#     g.output(trig, g.LOW)
#     while g.input(echo) == 0:
#         start = t.time()
#     while g.input(echo) == 1:
#         start = t.time()
#     duration = end - start
#     dis = round(duration * 17150, 2)
#     
#     print ("Distance: ") + dis
#     t.sleep(dur)


    
