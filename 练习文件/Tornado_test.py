#!/usr/bin/python3
# -*- coding:utf-8 -*-
#P-Name:    python_test
#F-Name:    Tornado_test.py
#Login:     Administrator   
#Descripton:
#Author:    Smartwy
#Date:      2019/2/25 8:59:33
#Version:

import tornado.ioloop
import tornado.web

class MHandler(tornado.web.RequestHandler):
	def get(self):
		self.write('hello world')

# 创建一个Application对象，并把一个正则表达式'/'和类名MainHandler传入构造函数：tornado.web.Application(...)
application = tornado.web.Application([(r'/index',MHandler)])

if __name__ == '__main__':
	# 执行Application对象的listen(...)	方法，即：application.listen(8888)
	application.listen(8808)
	# 执行IOLoop类的类的start()方法，即：tornado.ioloop.IOLoop.instance().start()
	tornado.ioloop.IOLoop.instance().start()



