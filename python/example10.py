#!/usr/bin/python
#coding=UTF-8

import time

print (time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))

time.sleep(5)

print (time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))


