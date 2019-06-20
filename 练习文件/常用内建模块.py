# -*- coding:utf-8 -*-
#Name:     
#Descripton:
#Author:    smartwy
#Date:     
#Version:

# from datetime import datetime
# import time
# now = datetime.now()
# print(now,'\n',type(now))
# dt = datetime(2018,8,4,11,20)
# print(dt)
# print(dt.timestamp(),time.time()) # timestamp显示的时间是1970年开始至今的秒数
# print(datetime.fromtimestamp(time.time())) # fromtimestamp将至今秒数转换规则日期显示
# print(datetime.utcfromtimestamp(time.time())) # 当前秒数转换UTC时间显示-格林威治
# # now,T_format = input("Please input you date:\nexp:'2015-6-1 18:19:59', '%Y-%m-%d %H:%M:%S:").split()
# # t = datetime.strptime('2015-6-1 18:19:59', '%Y-%m-%d %H:%M:%S:')
# # print(t)
'''
	datetime模块支持datetime与str之间互相转换，及加减，时区转换，
'''

# from collections import namedtuple
# '''
# namedtuple是一个函数，它用来创建一个自定义的tuple对象，并且规定了tuple元素的个数，
# 并可以用属性而不是索引来引用tuple的某个元素。
# '''
# point = namedtuple('zuobiao',['x','y'])
# p = point(123,234)
# print(p.x)
# print(p.y)
# print(True if isinstance(p, point) else False)
# print(True if isinstance(p, tuple) else False)

# from collections import deque
# '''
# deque 可以提高list的插入与删除效率，
# deque除了实现list的append()和pop()外，还支持appendleft()和popleft()，这样就可以非常高效地往头部添加或删除元素
# '''
# l1 = deque(['1','a','y'])
# l1.append('zhao')
# l1.appendleft('wangye')
# print(l1)
# l1.popleft()
# print(l1)

# from collections import defaultdict
# '''
# 	设置dict的默认返回值
# '''
# # dict1 = {'key1':'value1','key2':'value2'} # 暂时好像不支持这种赋值
# dict1 = defaultdict(lambda :'N/A')
# dict1['key1'] = 'value1'
# dict1['key2'] = 'value2'
# print(dict1['key1'])
# print(dict1['key2'])
# print(dict1['key3'])

# from collections import OrderedDict
# '''
# dict是无序的，根据key才可查询，ordereddict可使dict根据key变有序
# '''
# dd = {'k1':'v1','32':'v2','k3':'v3'}
# print(dd)
# dd = OrderedDict(dd)
# print(dd)

# from collections import Counter
#
# count = Counter()       # Counter 统计元素的数量
# str1 = 'wangye is yushuren'
# list2 = ['abc','abc','456']
# for i in list2:
# 	count[i] = count[i]+1
# print(count)

# import  base64
# '''
# base64是一种用64个字符来表示任意二进制数据的方法，
# Base64适用于小段内容的编码，比如数字证书签名、Cookie的内容等.不能用于加密
# '''
# b64 = base64.b64encode(b'i\xb7\x1d\xfb\xef\xff')
# print('1',b64)      # 输出包含//和++ 不能作为URL的参数，需要再转-或_,方可使用
# b64 = base64.b64decode(b64)
# print('2',b64)
# b64 = base64.urlsafe_b64encode(b'i\xb7\x1d\xfb\xef\xff') # 使用urlsafe编码的base64规范转换
# print('3',b64)
# nn = '在Python中使用BASE 64编码'.encode('utf-8')
# print('4',nn)
# s = base64.b64encode(nn)
# print('5',s)
# d = base64.b64decode(s).decode('utf-8')
# print('6',d)

# import base64
# def safe_base64_decode(s):
# 	pass
#
# # 测试:
# assert b'abcd' == safe_base64_decode(b'YWJjZA=='), safe_base64_decode('YWJjZA==')
# assert b'abcd' == safe_base64_decode(b'YWJjZA'), safe_base64_decode('YWJjZA')
# print('ok')

# import struct,base64
# '''
# strcut 可以将bytes与其它二进制类型进行转换
# '''
# s = 123456789
# p = struct.pack('>I',s) # pack 把任意类型转换为bytes，>表示字节顺序，网络序。I:4个字节无符号输出类型 https://docs.python.org/3/library/struct.html#format-characters
# print(p)
# p = struct.unpack('>I',b'\x07[\xcd\x15') # unpack 把bytes转换相应的类型
# print(p)

# import hashlib
#
# md5 = hashlib.md5()
# md5.update('wangye si yushu ren !'.encode('utf-8'))
# print(md5.hexdigest())
#
# md6 = hashlib.md5()
# md6.update('wangye si yu'.encode('utf-8'))
# md6.update('shu ren !'.encode('utf-8'))
# print(md6.hexdigest())
#
# sha1 = hashlib.sha1()
# sha1.update('wangye si yushu ren !'.encode('utf-8'))
# print(sha1.hexdigest())
#
# sha2 = hashlib.sha1()
# sha2.update('wangye si '.encode("utf-8"))
# sha2.update('yushu ren !'.encode('utf-8'))
# print(sha2.hexdigest())

# import hashlib
# md5 = hashlib.md5()
# # md5.update('wangye123456zhaomin'.encode('utf-8'))
# name = 'wangye'
# password = hashlib.md5('wangye123456zhaomin'.encode('utf-8')).hexdigest()
# iname,ipassword = input('Please input you name and password : ').split()
# if iname == name and password == hashlib.md5(str(iname+ipassword+'zhaomin').encode('utf-8')).hexdigest():
# 	print('Login ok')
# else:
# 	print('Login no')

# import random
#
# print(random.randint(555555,666666))
# print(random.randrange(666666))

# import hmac
#
# message = b'hello world'
# key = b'zhaomin'
# print(hmac.new(key,message,digestmod='MD5').hexdigest())

# import itertools
'''
itertools模块提供的全部是处理迭代功能的函数，它们的返回值不是list，而是Iterator，只有用for循环迭代的时候才真正计算。
'''
# n = itertools.count(1) # 实例一个无限迭代对象
# for i in n :
# 	print(i)
# 	if i >= 10 :
# 		break

# c = itertools.cycle('abcde') # cycle会把传进的序列无线循环
# for i in c :
# 	print(i)

# r = itertools.repeat('ABCDEF',3) # repeat 按设置参数迭代次数
# for i in r:
# 	print(i)

# ns = itertools.count(1)
# n = itertools.takewhile(lambda x : x <= 10,ns) # 根据takewhile的设置提取有限序列
# for i in n:
# 	print(i)

# it = [1,2,3]
# for i in itertools.chain('abc','def',it): # chain 可将多个迭代对象链接在一起进行迭代
# 	print(i)

# for key,grou in itertools.groupby('AajjJjjiiiwwwssssaa',lambda x : x.upper()): # 将相邻的迭代器元素挑出来,可忽略大小写
# 	print(key,list(grou))

# from contextlib import contextmanager
# '在某段代码执行前后自动执行特定代码,实现代码段的上下文管理'
# class Query(object):
#     def __init__(self, name):
#         self.name = name
#     def query(self):
#         print('Query info about %s...' % self.name)
# @contextmanager
# def create_query(name):
#     print('Begin')
#     q = Query(name)
#     yield q
#     print('End')
# with create_query('Bob') as q:
#     q.query()

# from contextlib import contextmanager
#
# @contextmanager
# def tag(name):
# 	print('1 %s'% name)
# 	yield
# 	print('2 %s'% name)
# with tag('wangye'):
# 	print('3')
# '''
# 代码的执行顺序是：
# 1, with语句首先执行yield之前的语句，因此打印出 1；
# 2, yield调用会执行with语句内部的所有语句，因此打印 3；
# 3, 最后执行yield之后的语句，打印出 2。
# 因此，@contextmanager让我们通过编写generator来简化上下文管理。
# '''

# from datetime import datetime
# with open(r'E:\python_test\test.txt','a') as f:
# 	time = str(datetime.now())
# 	f.write(time+'\n')
# with open(r'E:\python_test\test.txt') as f:
# 	data = f.read()
# print(data)

# from urllib import request
# '''
# 	get到指定url的的响应头信息，也可添加*.add_header()来模拟浏览器发送get请求，往request对象添加HTTP头，来模拟浏览器
# '''
# with request.urlopen('https://api.douban.com/v2/book/2129650') as f :
# 	data = f.read()
# 	print('1->status:',f.status,f.reason)
# 	for k,v in f.getheaders():
# 		print('2->%s : %s'% (k,v))
# 	print('3->data:',data.decode('utf-8'))

# from html.parser import HTMLParser
# from html.entities import name2codepoint
#
# class MyHTMLParser(HTMLParser):
#     def handle_starttag(self, tag, attrs):
#         print('1 启动标志 <%s>' % tag)
#     def handle_endtag(self, tag):
#         print('2 结束标志 </%s>' % tag)
#     def handle_startendtag(self, tag, attrs):
#         print('3<%s/>' % tag)
#     def handle_data(self, data):
#         print('4 数据 ',data)
#     def handle_comment(self, data):
#         print('5 注释 <!--', data, '-->')
#     def handle_entityref(self, name):
#         print('&%s;' % name)
#     def handle_charref(self, name):
#         print('&#%s;' % name)
# parser = MyHTMLParser()
# parser.feed('''<html>
# <head></head>
# <body>
# <!-- test html parser -->
#     <p>Some <a href=\"#\">html</a> HTML&nbsp;tutorial...<br>END</p>
# </body>
# </html>''')



























