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
        p.ChangeDutyCycle(1)
        print "angle : 1"
        time.sleep(2)
        p.ChangeDutyCycle(6)
        print "angle : 6"
        time.sleep(2)
        p.ChangeDutyCycle(10)
        print "angle : 10"
        time.sleep(2)
except KeyboardInterrupt:
    p.stop()
GPIO.cleanup()