# -*- coding:utf-8 -*-
#Name:     
#Descripton:
#Author:    smartwy
#Date:     
#Version:

import socket
import time
import sys

# s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# host = socket.gethostname()
# port = 1000
#
# s.connect((host,port))
# msg = s.recv(1024)
# s.close()
# print(msg.decode("utf-8"))

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(('10.130.229.164',9999))
print(s.recv(1024).decode('utf-8'))
for data in [b'wangye',b'zhaomin',b'fengwei']:
	s.send(data)
	print(s.recv(1024).decode('utf-8'))
s.send(b'exit')
# print(s.recv(1024).decode("utf-8"))
s.close()


