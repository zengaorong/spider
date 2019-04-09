#coding=utf-8
import threading

import time
def fun_timer():
    print('Hello Timer!')
    global timer
    timer = threading.Timer(5.5, fun_timer)
    timer.start()

def fun_timer1():
    print('Hello Timer------------------------!')
    global timer1
    timer1 = threading.Timer(5.5, fun_timer1)
    timer1.start()

timer = threading.Timer(1, fun_timer)
timer1 = threading.Timer(2, fun_timer1)

timer.start()
timer1.start()

time.sleep(15) # 15秒后停止定时器

timer.cancel()
timer1.cancel()