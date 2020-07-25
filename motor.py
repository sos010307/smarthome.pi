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
        time.sleep(1)
        p.ChangeDutyCycle(5)
        print "angle : 5"
        time.sleep(1)
        p.ChangeDutyCycle(8)
        print "angle : 8"
        time.sleep(1)
except KeyboardInterrupt:
    p.stop()
GPIO.cleanup()


출처: https://ljs93kr.tistory.com/40 [건프의 소소한 개발이야기]