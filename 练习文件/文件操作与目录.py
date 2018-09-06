# -*- coding:utf-8 -*-
#Name:     
#Descripton:
#Author:    smartwy
#Date:     
#Version:

import os

# print(os.name)
# # print(os.uname())           # windows 不提供uname函数
# print(os.environ)               # 环境变量
# print(os.environ.get('python')) # 获取某个变量值
# print(os.path.abspath('.'))     # 获取绝对路径
# print(os.path.isdir(os.path.abspath('.')))
# print(os.path.abspath('.')+r'\file1')
#
# # os.mkdir(r'E:\testdir')
# # os.rmdir(r'E:\testdir')
# print(os.path.join(r'E:\testdir','yuyu'))
# # print(os.path.split(r'E:\testdir\yuyu'))
# y = os.path.splitext(r'E:\testdir\yuyu\uu.tst')
# print(y[1])

print([x for x in os.listdir('.') if os.path.isdir(x)])
print([x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1] == '.py'])







