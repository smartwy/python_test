#!/usr/bin/python3
# -*- coding:utf-8 -*-
#Name:     
#Descripton:
#Author:    smartwy
#Date:     
#Version:

from socket import *
from time import ctime
import os
ts = socket(AF_INET, SOCK_STREAM)
try:
	ts.bind(('192.168.10.244', 80))
except BaseException as e:
	print('bind error !',e)
	ts.close()
	exit('001')
try:
	ts.listen(5)
except BaseException as e:
	print('listen error !', e)
	ts.close()
print(gethostbyname_ex('www.butel.com'))
while True:
	print('start ...')
	tcpclientsock, addr = ts.accept()
	print('connet ', addr)
	while True:
		data = tcpclientsock.recv(1024)
		if not data or data.decode('utf-8') == 'exit':
			break
		else:
			print('%s 客户端信息 : %s' % (ctime(),data.decode('utf-8')))
			info = input('please input messages :')
			tcpclientsock.send(info.encode('utf-8'))
	tcpclientsock.close()



