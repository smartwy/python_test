#!/usr/bin/python3
# -*- coding:utf-8 -*-
#P-Name:    python_test
#F-Name:    进程池间Queue通讯.py
#Login:     Administrator   
#Descripton:
#Author:    Smartwy
#Date:      2019/6/20 10:53:38
#Version:



from multiprocessing import Manager, Pool, Queue
import os,time,random

def read(q):
	print('read func run %s master id:%s' % (os.getpid(), os.getppid()))
	for k,v in q.items():
		# print('Queue get  ')
		print('q.key:%s, q.value:%s' % (k, v))

def writer(q):
	print('writer func run %s '% os.getpid())
	for idx,i in enumerate('abcdef'):
		# q.put(i)
		q[idx] = i

if __name__ == '__main__':
	print('----start----id:%s' % os.getpid())
	# q = Manager().Queue() # 如果使用Queue会报错
	# q = Queue()
	q = Manager().dict() # 字典通讯
	p = Pool()
	p.apply_async(writer, (q,))
	time.sleep(1)
	p.apply_async(read, (q,))
	p.close()
	p.join()
	# print(q)
	print('-----end------')
