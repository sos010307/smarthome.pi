import RPi.GPIO as GPIO
import time
 
pin = 19 # PWM pin num 18
 
GPIO.setmode(GPIO.BCM)
GPIO.setup(pin, GPIO.OUT)
p = GPIO.PWM(pin, 50)
p.start(0)
cnt = 0
try:
    while True:
        p.ChangeDutyCycle(20)
        print "angle : 20"
        time.sleep(2)
        p.ChangeDutyCycle(15)
        print "angle : 15"
        time.sleep(2)
        p.ChangeDutyCycle(30)
        print "angle : 30"
        time.sleep(2)
except KeyboardInterrupt:
    p.stop()
GPIO.cleanup()