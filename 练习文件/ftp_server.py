#!/usr/bin/python3
# -*- coding:utf-8 -*-
#Name:     
#Descripton:
#Author:    smartwy
#Date:     
#Version:


from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer

obj = DummyAuthorizer()
obj.add_user('admin', '123456', 'E:\\截图', 'elradfmw') # 用户名，密码，共享目录， 权限
hand = FTPHandler
hand.authorizer = obj
server = FTPServer(('192.168.10.241', 21), hand)
server.serve_forever()


