#!/usr/bin/python3
# -*- coding:utf-8 -*-
#Name:     
#Descripton:
#Author:    smartwy
#Date:     
#Version:

import time
def decorator(fun):
	def wrapper(name): # name 是被装饰函数的参数
		print('start wrapper args : ',name)
		start = time.time()
		fun(name) # 注意是装饰器参数传递的函数对象，fun就是被装饰函数的另一个名称
		print('end wrapper ', time.time()-start)
	return wrapper

@decorator
def do_something(args):
	time.sleep(2)
	print('start do_something  ' + args)

do_something('wangye start')



