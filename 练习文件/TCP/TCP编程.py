# -*- coding:utf-8 -*-
#Name:     
#Descripton:
#Author:    smartwy
#Date:     
#Version:

import socket

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(('www.sohu.com', 80))
# s.bind(('www.sina.com.cn',80))

s.send(b'GET / HTTP/1.1\r\nHost: www.sohu.com\r\nConnection: close\r\n\r\n')
buffer = []
while 1:
	d = s.recv(1024)
	if d :
		buffer.append(d)
	else:
		break
data = b''.join(buffer) # 使用空字节把buffer字节列表链接一起，成为新的字节串。例如： '_'.join('abc'); 输出a_b_c
# print(s.getpeername()) # 获取远端地址与端口 ， 元组显示
s.close()

header, html = data.split(b'\r\n\r\n',1)
print(header.decode('utf-8'))
with open('sohu.html','wb') as f:
	f.write(html)

# a,b = 0,1
# while b <= 100:
# 	print(b)
# 	a,b = b,b+a