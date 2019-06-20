#!/usr/bin/python3
# -*- coding:utf-8 -*-
#P-Name:    python_test
#F-Name:    协程gevent.py
#Login:     Administrator   
#Descripton:
#Author:    Smartwy
#Date:      2019/2/25 17:33:40
#Version:

# 自动切换，有I/O 或sleep
import gevent
import time

def fun1():
	print('1')
	gevent.sleep(2)
	print('2')
def fun2():
	print('3')
	gevent.sleep(5)
	print('4')

start = time.time()

gevent.joinall(
	[gevent.spawn(fun1),
	 gevent.spawn(fun2)]
)
print(time.time()-start)

