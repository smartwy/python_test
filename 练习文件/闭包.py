#!/usr/bin/python3
# -*- coding:utf-8 -*-
#Name:     
#Descripton:
#Author:    smartwy
#Date:     
#Version:

# 一个内嵌函数引用了外部变量(不是全局变量)，且这个外部函数返回内嵌函数，称之为闭包
def fun(num):
	def funchild():
		return num*2
	return funchild()
res = fun(666)
print(res)


