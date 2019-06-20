#!/usr/bin/python3
# -*- coding:utf-8 -*-
#P-Name:    python_test
#F-Name:    yaml_pro.py
#Login:     Administrator   
#Descripton:
#Author:    Smartwy
#Date:      2019/3/8 6:38:28
#Version:

'''
yaml.load(f) 返回一个对象
yaml.load_all(f) 生成一个迭代器， .yaml文件中是使用 --- 分割迭代元素
yaml.dump(data,f) python对象生成yaml格式数据,接收的第二个参数一定要是一个打开的文本文件或二进制文件
yaml.dump_all([data1,data2],f) 多段python对象生成yaml格式数据保存文件中,接收的末位参数一定要是一个打开的文本文件或二进制文件

1. 大小写敏感
2. 使用缩进表示层级关系
3. 缩进时不允许使用Tab，只允许使用空格
4. 缩进的空格数目不重要，只要相同层级的元素左对齐即可
5. # 表示注释，从它开始到行尾都被忽略
'''


import yaml

with open('config.yaml','w',encoding='utf-8') as f:
	# a = yaml.load(f) # 载入文件内容
	# print(a['manages'][0]['admin'])
	# print(a)
	# b = yaml.load_all(f)
	# for i in b:
	# 	print(i)
	# aproject = {'name': 'Silenthand Olleander',
	#        'race': 'Human',
	#        'traits': ['ONE_HAND', 'ONE_EYE']
	#       }
	aproject1 = {'mather': 'ttng',
	             'father': 'ttng',
	             'test': 'uiui'
	             }
	# yaml.dump(aproject,f)
	aproject = {'name': 'Silenthand Olleander',
	            'race': 'Human',
	            'traits': 'ONE_HAND'
	            }
	# yaml.dump(aproject,f)
	# print(result)
	yaml.dump_all([aproject,aproject1], f)

