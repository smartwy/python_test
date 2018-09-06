# -*- coding:utf-8 -*-
#Name:     
#Descripton: 把变量从内存中变成可存储或传输的过程称之为序列化
#Author:    smartwy
#Date:     
#Version:

import pickle
#
# d = input('Please input you name:')
# print(pickle.dumps(d))
# f = open('file1','ab')
# pickle.dump(d,f)     # 内存转存到存储盘
# f.close()

# f = open('file1','rb')
# t = pickle.load(f)      # 存储读出到内存
# f.close()
# print(t)
# s = input('Please input :')
# f = open('file1','a')
# f.write(s)
# f.close()
arg = input('read data-> r or write data-> w :')
if arg == 'w' or arg == 'W':
	'''
	将UI输入存储到磁盘上，
	'''
	d1 = input('Please input :')
	f1 = open('file1','wb')
	pickle.dump(d1,f1)
	f1.close()
elif arg == 'r' or arg == 'R':
	'''
	将磁盘数据读出到内存
	'''
	f2 = open('file1','rb')
	du = pickle.load(f2)
	print(du)
	f2.close()
else:
	raise TypeError('you input error! (r or w)')
