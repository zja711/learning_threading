# -*- coding: UTF-8 -*-
import threading
from datetime import datetime
import time
import logging

""""

"""


def run_c1():
    time.sleep(5)
    for i in range(30):
        print "c1-%s\n" % i


def run_c2():
    time.sleep(5)
    for i in range(20):
        print "c2-%s\n" % i


def run_c3():
    time.sleep(5)
    for i in range(50):
        print("c3-%s\n" % i)

c1 = threading.Thread(name="c1",target=run_c1)
c2 = threading.Thread(name="c2",target=run_c2)
c3 = threading.Thread(name="c3",target=run_c3)
c3.setDaemon(True)  # 设为守护进程，随主进程终止而终止

print 'start ...\n'
c1.start()
c2.start()
# c3.start()

c1.join(3)  # 5秒之后，join超时，此时c1仍继续执行，但主线程不再等待c1
c2.join()   # 无设置超时时间，主线程挂起，等待c2,c3执行完毕
print "isAlive:"+str(c1.isAlive())+'\n'    # c1未执行完毕，则isAlive为True
print 'the end ...\n'   # 需等待c2执行完毕；需等待至c1的join超时或者c1执行完毕
