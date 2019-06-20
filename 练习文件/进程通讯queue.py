#!/usr/bin/python3
# -*- coding:utf-8 -*-
#P-Name:    python_test
#F-Name:    进程通讯queue.py
#Login:     Administrator   
#Descripton:
#Author:    Smartwy
#Date:      2019/2/25 16:35:12
#Version:



from multiprocessing import Process, Queue
import queue


def f(q,n):
	# q.put([123, 456, 'hello'])
	q.put(n * n + 1)
	print("son process", id(q))


if __name__ == '__main__':
	q = Queue()  # try: q=queue.Queue()
	print("main process", id(q))

	for i in range(3):
		p = Process(target=f, args=(q,i))
		p.run() # 运行在主进程，将f函数作为参数传递给主进程。main id
		p.start() # 启动子进程，son id

	print(q.get())
	print(q.get())
	print(q.get())


