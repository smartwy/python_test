# -*- coding:utf-8 -*-
#Name:     
#Descripton:
#Author:    smartwy
#Date:     
#Version:

import unittest

from myDict import Dict

class TestDict(unittest.TestCase):              #从unittest.TestCase继承，以test开头的都是测试方法，被执行
	def setUp(self):
		print('测试前执行的，例如打开数据库或文件')
	def test_init(self):
		d = Dict(a=1,b=2)
		self.assertEqual(d.a,1)                 # 断言d.a是否等于1
		self.assertEqual(d.b,2)
		self.assertTrue(isinstance(d,dict))     #断言d是否是dict类对象
		print('1')
	def test_key(self):
		d = Dict()
		d['k1'] = 'v1'
		self.assertEqual(d['k1'],'v1')
		print('2')
	def test_attr(self):
		d = Dict()
		d.key = 'value'
		self.assertTrue('key' in d)
		self.assertEqual(d.key,'value')
		print('3')
	def test_keyerror(self):
		d = Dict()
		with self.assertRaises(KeyError):
			value = d['empty']
		print('4')
	def test_attrerror(self):
		d = Dict()
		with self.assertRaises(AttributeError):
			value = d.empty
		print('5')
	def tearDown(self):
		print('测试后执行的，例如关闭数据库或文件')

if __name__ == '__main__':
	unittest.main()