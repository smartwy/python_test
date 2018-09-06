# -*- coding:utf-8 -*-
#Name:     
#Descripton:
#Author:    smartwy
#Date:     
#Version:

# import os,stat
#
# try:
# 	if os.path.isdir(r'E:\python_test\练习文件'):
# 		f = open('file1','r')
# 		print(f.read())
# except:
# 	pass
# finally:
# 	f.close()           # 无论是否出错，都能正确关闭文件，
#
# with open('file1','a') as f:
# 	f.write('\n**************************')
#
# s = os.stat('file1')  # 获取文件所有属性
# print(s)

from io import StringIO

f = StringIO()
f.write('hello world !')
print(f.getvalue())             #使用getvalue获取写入后的str
i = StringIO('hello\nworld!')
while True:
	s = i.readline()
	if s == '':
		break
	print(s.strip())

# from io import BytesIO
#
# f = BytesIO()
# f.write('中文'.encode('utf-8'))
# print(f.getvalue())
#
# i = BytesIO(b'\xe4\xb8\xad\xe6\x96\x87')
# print(i.read())










