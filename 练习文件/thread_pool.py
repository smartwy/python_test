#!/usr/bin/python3
# -*- coding:utf-8 -*-
#Name:     
#Descripton:
#Author:    smartwy
#Date:     
#Version:

import os, time, random
# from multiprocessing.Queue import *
from multiprocessing import Queue
from threading import Thread

class MyPool():
	def __init__(self, ths):
		if ths is None:
			ths = os.cpu_count() or 1
		if ths < 1:
			raise ValueError('MyPool(*):*参数有误！')
		self.ths = ths
		self.queue = Queue()
		for i in range(self.ths):
			t = Thread(target=self.job)
			t.start()
	def job(self):
		while True:
			func, args, kwargs = self.queue.get()
			func(*args, **kwargs)
			self.queue.join_thread()
	def apply_async(self,func,args=(), kwargs=None):
		if kwargs is None:
			kwargs = {}
		self.queue.put((func, args, kwargs))
	def join(self):
		self.job().join()

def task1(*args, **kwargs):
	print('执行task1')
	print('参数：', args, kwargs)
	time.sleep(random.randint(1,3))
	print('结束task1')

def task2():
	print('执行task2')
	time.sleep(random.randint(1,3))
	print('结束task2')

if __name__ == '__main__':
	pool = MyPool(2)
	pool.apply_async(task1, args=(1,2), kwargs={'e':3, 'w':'1'})
	pool.apply_async(task2)
	print('任务提交完成')
	pool.join()
	print('任务执行完毕')

