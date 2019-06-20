#!/usr/bin/python3
# -*- coding:utf-8 -*-
#P-Name:    python_test
#F-Name:    进程间通讯manager.py
#Login:     Administrator   
#Descripton:
#Author:    Smartwy
#Date:      2019/2/25 16:38:43
#Version:

# Python中进程间共享数据，处理基本的queue，pipe和value + array外，还提供了更高层次的封装。
# 使用multiprocessing.Manager可以简单地使用这些高级接口。
# Manager()返回的manager对象控制了一个server进程，此进程包含的python对象可以被其他的进程通过proxies来访问。从而达到多进程间数据通信且安全。
# Manager支持的类型有list, dict, Namespace, Lock, RLock, Semaphore, BoundedSemaphore, Condition, Event, Queue, Value和Array。

# manager 实现了进程间的数据交互与共享
from multiprocessing import Process, Manager


def f(d, l, n):
	d[n] = n
	d["name"] = "xuyaping"
	l.append(n)

if __name__ == '__main__':
	with Manager() as manager:
		d = manager.dict()
		l = manager.list(range(5))
		p_list = []
		for i in range(10):
			p = Process(target=f, args=(d, l, i))
			p.start()
			p_list.append(p)
		for res in p_list:
			res.join()
		print('d-->',d)
		print('l-->',l)


