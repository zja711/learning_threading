# -*- coding: UTF-8 -*-
import threading
from threading import Timer
from datetime import datetime


def hello(start):
    print "hello, world"
    print datetime.now() - start


t = Timer(5, hello, args=(datetime.now(),))
t.start()  # after 30 seconds, "hello, world" will be printed
