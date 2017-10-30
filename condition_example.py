# -*- coding: UTF-8 -*-
"""
notify()及notifyAll()并不会释放锁，意味着所要唤醒的线程不会马上从wait()返回，
只有当调用notify()或者notifyAll()的线程放弃锁的所有权

"""
import threading
import time
from threading import Lock


def producer(cv):
    print "this is producer\n"
    with cv:
        for i in range(3):
            print "     producing ...%s\n" % i
            time.sleep(1)
        cv.notifyAll()
        print "producer notify all ...\n"


def consumer(cv):
    print "this is consumer\n"
    with cv:
        print "consumer wait ...\n"
        cv.wait()
        print "consuming ...\n"


"""
lock = threading.RLock()
condition_1 = threading.Condition(lock)
condition_2 = threading.Condition(lock)
参见 http://effbot.org/zone/thread-synchronization.htm
"""
condition = threading.Condition()

t1 = threading.Thread(name="consumer", target=consumer, args=(condition,))
t2 = threading.Thread(name="producer", target=producer, args=(condition,))

print 'start ...\n'
t1.start()
t2.start()

t1.join()
t2.join()

print "the end ...\n"
