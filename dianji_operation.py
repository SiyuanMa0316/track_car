#try:
import RPi.GPIO as GPIO
#except RuntimeError:
#    print "GPIO error"

import time,sys
IN1,IN2,IN3,IN4=22,18,13,11
arr=[22,18,13,11]
GPIO.setwarnings(False)
def init():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(22,GPIO.OUT)
    GPIO.setup(18,GPIO.OUT)
    GPIO.setup(13,GPIO.OUT)
    GPIO.setup(11,GPIO.OUT)
    
def t_stop(sleep_time):
    init()
    time.sleep(sleep_time)
    GPIO.cleanup()

def t_up(sleep_time,dutyratio,fre=100):
    init()
    p1=GPIO.PWM(IN1,fre)
    p1.start(dutyratio)
    p2=GPIO.PWM(IN2,fre)
    p2.start(0)
    p3=GPIO.PWM(IN3,fre)
    p3.start(dutyratio)
    p4=GPIO.PWM(IN4,fre)
    p4.start(0)
    time.sleep(sleep_time)
    GPIO.cleanup()

def t_down(sleep_time,dutyratio,fre=100):
    init()
    p1=GPIO.PWM(IN1,fre)
    p1.start(0)
    p2=GPIO.PWM(IN2,fre)
    p2.start(dutyratio)
    p3=GPIO.PWM(IN3,fre)
    p3.start(0)
    p4=GPIO.PWM(IN4,fre)
    p4.start(dutyratio)
    time.sleep(sleep_time)
    GPIO.cleanup()

def t_right(sleep_time,dutyratio_left,dutyratio_right,fre=100):
    init()
    p1=GPIO.PWM(IN1,fre)
    p1.start(70)
    p2=GPIO.PWM(IN2,fre)
    p2.start(0)
    p3=GPIO.PWM(IN3,fre)
    p3.start(0)
    p4=GPIO.PWM(IN4,fre)
    p4.start(70)
    time.sleep(sleep_time)
    GPIO.cleanup()
    
def t_left(sleep_time,dutyratio_left,dutyratio_right,fre=100):
    init()
    p1=GPIO.PWM(IN1,fre)
    p1.start(0)
    p2=GPIO.PWM(IN2,fre)
    p2.start(70)
    p3=GPIO.PWM(IN3,fre)
    p3.start(70)
    p4=GPIO.PWM(IN4,fre)
    p4.start(0)
    time.sleep(sleep_time)
    GPIO.cleanup()

if __name__=='__main__':
    t_up(3,60)
    t_down(3,30)
    #t_left(1,70,70)
    #t_right(1,60,60)
    #t_stop(1)
