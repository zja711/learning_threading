# -*- coding: UTF-8 -*-
import threading
import time
from threading import Lock

count = 0
lock = Lock()


def run_c1():
    global count
    lock.acquire(True)
    print "c1 acquired lock ...\n"
    for i in range(50):
        count += 1
        print "c1-%s:count=%s\n" % (i, count)


def run_c2():
    global count
    lock.acquire(True)
    print "c2 acquired lock ...\n"
    for i in range(50):
        count += 1
        print "c2-%s:count=%s\n" % (i, count)


def run_c3():
    global count
    while True:
        if count == 30:
            print "c3 released lock"
            lock.release()


c1 = threading.Thread(name="c1", target=run_c1)
c2 = threading.Thread(name="c2", target=run_c2)
c3 = threading.Thread(name="c2", target=run_c3)
c3.setDaemon(True)

print 'start ...\n'
c1.start()
c2.start()
c3.start()

c1.join()
c2.join()

print "the end ...\n"
