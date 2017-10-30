# -*- coding: UTF-8 -*-
import threading
from threading import BoundedSemaphore
from datetime import datetime
import time


"""
使用场景：
Semaphores are often used to guard resources with limited capacity, for example, a database server
"""
maxconnections = 3
pool_sema = BoundedSemaphore(value=maxconnections)


def consume():
    pool_sema.acquire()
    print "%s:consuming ...%s\n" % (threading.currentThread(),datetime.now())
    time.sleep(5)
    pool_sema.release()


for i in range(10):
    name = "Thread_%s" % i
    threading.Thread(name=name, target=consume).start()



