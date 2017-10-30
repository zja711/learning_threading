# -*- coding: UTF-8 -*-
import threading
from threading import Event
import time


def run_t1(e):
    e.clear()
    print "t1 is running ...\n"
    for i in range(10):
        print "     t1:%s" % i
        time.sleep(0.5)
        if i == 5:
            e.set()
            print "     enable t2 ...\n"


def run_t2(e):
    print "t2 is waiting ...\n"
    e.wait()
    print "t2 is running ...\n"
    for i in range(10):
        time.sleep(1)
        print "     t2:%s" % i


event = Event()
t1 = threading.Thread(name="c1", target=run_t1, args=(event,))
t2 = threading.Thread(name="c2", target=run_t2, args=(event,))

t1.start()
t2.start()
