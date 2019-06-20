#!/usr/bin/python3
# -*- coding:utf-8 -*-
#P-Name:    python_test
#F-Name:    协程greenlet.py
#Login:     Administrator   
#Descripton:
#Author:    Smartwy
#Date:      2019/2/25 17:26:35
#Version:


# 手动切换
from greenlet import greenlet

def foo():
	print('foo start ')
	grn2.switch()
	print('foo end ')
	grn2.switch()

def foo2():
	print('foo2 start ')
	grn1.switch()
	print('foo2 end ')

grn1 = greenlet(foo)
grn2 = greenlet(foo2)

grn1.switch()



