# -*- coding:utf-8 -*-
#Name:     
#Descripton:
#Author:    smartwy
#Date:     
#Version:

import threading,os,time

local_school = threading.local()        # 创建全局threadlocal对象 用于局部变量的传递,每个线程只能访问自己创建的变量
def process_student():
	std = local_school.student
	scroe = local_school.scroe
	print('Hello %s you scroe is %s (in %s)'%(std,scroe,threading.current_thread().name))
	print(os.getpid())
	time.sleep(3)
def process_thread(name,number):
	local_school.student = name
	local_school.scroe = number
	process_student()
if __name__ == '__main__':
	t1 = threading.Thread(target=process_thread, args=('alice','89'), name='thread---A')
	t2 = threading.Thread(target=process_thread, args=('bob','99'), name='thread---B')
	t1.start()
	t2.start()
	t1.join()           # 使用join是为了阻塞当前线程(即主线程)，直到当前子线程结束后才继续往下执行，如果不需等待线程执行完可以不用
	print('test t1.join() block ability ！')
	t2.join()
	print('test t2.join() block ability ！')





