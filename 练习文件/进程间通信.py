# -*- coding:utf-8 -*-
#Name:     
#Descripton:
#Author:    smartwy
#Date:     
#Version:

from multiprocessing import Process,Queue
import os,time,random

def write(q):
	print('Process to write: %s '% os.getpid())
	for value in ['A','B','C']:
		print('Put %s to queue..'% value)
		q.put(value)                # 写数据到q对象
		time.sleep(random.random())
def read(q):
	print('Process to read %s '% os.getpid())
	while True:
		value = q.get(True)         # 从q对象里取数据
		print('get %s from queue' % value)
if __name__ =='__main__':
	q = Queue()
	pw = Process(target=write,args=(q,))
	pr = Process(target=read,args=(q,))
	pw.start()
	pr.start()
	pw.join()
	pr.terminate()  #read函数进入死循环，只能强行终止



