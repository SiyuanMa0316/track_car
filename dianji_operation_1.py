import RPi.GPIO as GPIO
import tkinter as tk
import time,sys

window=tk.Tk()
window.title('Move')
IN1,IN2,IN3,IN4=22,18,13,11
GPIO.setwarnings(False)


def init():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(22,GPIO.OUT)
    GPIO.setup(18,GPIO.OUT)
    GPIO.setup(13,GPIO.OUT)
    GPIO.setup(11,GPIO.OUT)

def move_forward():
    init()
    
    p1=GPIO.PWM(22,100)
    p1.start(70)
    p2=GPIO.PWM(18,100)
    p2.start(0)
    p3=GPIO.PWM(13,100)
    p3.start(70)
    p4=GPIO.PWM(11,100)
    p4.start(0)
    time.sleep(1)
    # GPIO.cleanup()

def move_back(sleep_time=1,fre=100,zhankb2=60,zhankb4=60):
    init()
    p1=GPIO.PWM(22,fre)
    p1.start(0)
    p2=GPIO.PWM(IN2,fre)
    p2.start(30)
    p3=GPIO.PWM(IN3,fre)
    p3.start(0)
    p4=GPIO.PWM(IN4,fre)
    p4.start(30)
    time.sleep(sleep_time)
    # GPIO.cleanup()

def move_right(sleep_time=1,fre=100,zhankb=30):
    init()
    p1=GPIO.PWM(22,fre)
    p1.start(70)
    p2=GPIO.PWM(IN2,fre)
    p2.start(0)
    p3=GPIO.PWM(IN3,fre)
    p3.start(0)
    p4=GPIO.PWM(IN4,fre)
    p4.start(70)
    time.sleep(sleep_time)
    #GPIO.cleanup()
    
def move_left(sleep_time=1,fre=100,zhankb=70):
    init()
    p1=GPIO.PWM(22,fre)
    p1.start(0)
    p2=GPIO.PWM(IN2,fre)
    p2.start(70)
    p3=GPIO.PWM(IN3,fre)
    p3.start(70)
    p4=GPIO.PWM(IN4,fre)
    p4.start(0)
    time.sleep(sleep_time)
    #GPIO.cleanup()

button_move_forward=tk.Button(window,text='forward',command=move_forward)
button_move_forward.pack()

button_move_back=tk.Button(window,text='back',command=move_back)
button_move_back.pack()

button_move_right=tk.Button(window,text='right',command=move_right)
button_move_right.pack()

button_move_left=tk.Button(window,text='left',command=move_left)
button_move_left.pack()

window.mainloop()
