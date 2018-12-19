import RPi.GPIO as GPIO
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

def motor(delay_time,dutyratio_leftforward,dutyratio_leftbackward,
          dutyratio_rightforward,dutyratio_rightbackward,fre=100):
    init()
    p1=GPIO.PWM(IN1,fre)
    p1.start(dutyratio_leftforward)
    p2=GPIO.PWM(IN2,fre)
    p2.start(dutyratio_leftbackward)
    p3=GPIO.PWM(IN3,fre)
    p3.start(dutyratio_rightforward)
    p4=GPIO.PWM(IN4,fre)
    p4.start(dutyratio_rightbackward)
    time.sleep(delay_time)
    GPIO.cleanup()
#if __name__=='__main__':
   #motor(1,0,60,0,60)
