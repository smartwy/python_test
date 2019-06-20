#!/usr/bin/python3
# -*- coding:utf-8 -*-
#P-Name:    python_test
#F-Name:    全局解释器锁.py
#Login:     Administrator   
#Descripton:
#Author:    Smartwy
#Date:      2019/6/20 14:28:47
#Version:


import threading
import time

class MyThread(threading.Thread):

	def run(self):
		global num
		time.sleep(1)
		if mutex.acquire(): # 上锁
			num += 1
			msg = self.name + ' set num to ' + str(num)
			print(msg)
			mutex.release() # 解锁
		# if num % 4 == 0:
		# 	mutex.acquire()
		# 	num += 1
		# 	msg = self.name + ' set num to ' + str(num)
		# 	print(msg)
		# 	mutex.release()  # 解锁
		# else:
		# 	num += 1
		# 	msg = self.name + ' set num to ' + str(num)
		# 	print(msg)

num = 0
mutex = threading.Lock()

def test():
	for i in range(5):
		t = MyThread()
		t.start()
		# t.join() # 不用锁，使用join也可正常操作同一数据，效率很低

if __name__ == "__main__":
	# s = time.time()
	test()
	# print(time.time() - s)


