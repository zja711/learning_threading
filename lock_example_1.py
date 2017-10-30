# -*- coding: UTF-8 -*-
import threading
import time
from threading import Lock


count = 0
lock = Lock()


def run_c1():
    global count
    print "c1 sleeping ...\n"
    time.sleep(1)
    with lock:
        print "c1 acquire lock ...\n"
        for i in range(50):
            count += 1
            print "c1-%s:count=%s\n" % (i,count)


def run_c2():
    global count
    with lock:
        print "c2 acquire lock ...\n"
        print "c2 sleeping ...\n"
        time.sleep(1)
        for i in range(50):
            count += 1
            print "c2-%s:count=%s\n" % (i, count)

c1 = threading.Thread(name="c1",target=run_c1)
c2 = threading.Thread(name="c2",target=run_c2)

print 'start ...\n'
c1.start()
c2.start()

c1.join()
c2.join()

print "the end ...\n"


