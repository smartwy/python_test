# -*- coding:utf-8 -*-
#Name:     
#Descripton:
#Author:    smartwy
#Date:     
#Version:

import socket
import threading
import time
import sys
# #创建套接字
# serversocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# #定义主机端口
# host = socket.gethostname()
# port = 1000
# #绑定主机与端口
# serversocket.bind((host,port))
# #设置最大连接数，超出排队
# serversocket.listen(5)
# while True:
# 	# 等待客户端进行访问
# 	clientsocket,addr = serversocket.accept()
# 	print("链接地址为： %s " % str(addr))
# 	msg = '欢迎菜鸟来访！'+"\r\n"
# 	# 发送给客户端的内容
# 	clientsocket.send(msg.encode("utf-8"))
# 	clientsocket.close()

def tcplink(sock,addr):
	print('connection ok %s:%s' % addr)
	sock.send(b'Welcome')
	while True:
		data = sock.recv(1024) # 如果使用UDP，需使用recvfrom() 注意：从服务端接收数据仍然使用recv()
		# time.sleep(1)
		if not data or data.decode('utf-8') == 'exit':
			break
		sock.send(('hello %s ' % data.decode('utf-8')).encode('utf-8')) # 如果使用UDP，需使用sendto()
	sock.close()
	print('close from  %s :%s link !' % addr)

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(('192.168.10.241',9999))
s.listen(5) # 连接数量， 如果使用UDP，不需要listen
print('waiting for connection ...')
while True:
	sock,addr = s.accept() # 等待客户端访问，阻塞式 如果使用UDP，不需使用accept
	print('start threading ..')
	t = threading.Thread(target=tcplink, args=(sock, addr))
	t.start()





