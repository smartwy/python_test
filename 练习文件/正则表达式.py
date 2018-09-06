# -*- coding:utf-8 -*-
#Name:     
#Descripton:
#Author:    smartwy
#Date:     
#Version:

# import re
# flag = 1
# f = open('E:\\python_test\\test.txt','r')
# line = len(f.readlines())
# f.close()
# fd = open('E:\\python_test\\test.txt','r')
# while flag <= line:
# 	f_data = fd.readline()
# 	num = re.match(r'.*\s*\w{3,7}@.*com',f_data)
# 	if  num :
# 		print('serach ok ! in file %s !'% flag)
# 		print(f_data)
# 	flag+=1
# fd.close()

# import re
# '''
# 	group 分组：使用（）标识分组，使用group(n)表示第n组
# 	group() == group(0) :输出匹配到的完整字符串
# 	group(1) : 输出正则表达式的从左向右第一个（）所匹配到的字符串
# 	group(3) ：输出正则表达式的从左向右第三个（）所匹配到的字符串，例如下列代码使用（3）会报错，因为正则表达式内没有第三个()
# 	groups(): 以元组格式输出所有分组内容
# '''
# line = "Cats are smarter than dogs"
# matchObj = re.match(r'(.*) are (.*?) .*', line)
# if matchObj:
# 	print("matchObj.group() : ", matchObj.group())
# 	print("matchObj.group(1) : ", matchObj.group(1))
# 	print("matchObj.group(2) : ", matchObj.group(2))
# 	print('matchObj.groups()',matchObj.groups())
# else:
# 	print("No match!!")

import re

# line = 'cats are smarter than dogs'
# try:
# 	serach_obj = re.search(r'(.*) are (.*?) .*', line)
# 	print("serach :",serach_obj.group())
# 	print('serach :',serach_obj.group(1))
# 	print("serach :",serach_obj.group(2))
# except IndexError:   # group(3)报错，会执行
# 	print('No found search !')
# else:
# 	pass

# line = 'cats are smarter than dogs'
# matchobj = re.match(r'dogs',line)       # re.match 只匹配字符串开始 不匹配则失败
# if matchobj:
# 	print("matchobj : ",matchobj.group())
# else:
# 	print('No match')
# serachobj = re.search(r'dogs',line)     # re.serach 匹配整个字符串 serach到最后
# if serachobj:
# 	print('serachobj :',serachobj.group())
# else:
# 	print("No serach ")

# import re
#
# phone = '010-8899773883442-233 # 这是一个电话号码'
#
# num = re.sub(r'#.*$','',phone)
# print(num)
# num = re.sub(r'\D','',phone)
# print(num)
# num = re.search(r'(88)\d+\1',phone)
# print(num)

# import re
#
# string = 'abcdefg hijklm npoqrst   uvwxyz'
# num = re.split(r'\s+',string) # 以一个或多个空格作为切分代码
# print(num)
# string = 'abcdefg，hijklm，npo qrst   uvwxyz'
# num = re.split(r'[\s\,]+',string) # 以一个或多个空格或‘，’作为切分代码
# print(num)


import re
num = '010-12345'
try:
	re_telephone = re.compile(r'^(\d{3})-(\d{3,8})$')  # 预编译正则表达式 如果后面程序经常使用相同的正则，使用预编译可以提高效率
	print(re_telephone.match(num).groups())
	print(re_telephone.match(num).group())
	print(re_telephone.match(num).group(1))
	print(re_telephone.match(num).group(2))
except TypeError or IndexError:
	print('正则表达式有问题，请检查！')
