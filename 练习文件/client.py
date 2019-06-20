#!/usr/bin/python3
# -*- coding:utf-8 -*-
#Name:     
#Descripton:
#Author:    smartwy
#Date:     
#Version:


from socket import *
from time import ctime
ts = socket()
ts.connect(('192.168.10.241', 80))
ts.send(b'client')
while True:
	data = ts.recv(1024)
	if not data or data.decode('utf-8') == 'exit':
		print('close !')
		break
	else:
		print('%s 服务端信息 : %s' % (ctime(), data.decode('utf-8')))
		info = input('please input messages :')
		ts.send(info.encode('utf-8'))
ts.close()


