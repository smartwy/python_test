'''
# 初始化城市信息
city_dict = {'广州': {'天河': ['天河体育馆', '金山大夏'],
                    '越秀': ['越秀公园', '光孝寺'],
                    '番禺': ['长隆欢乐世界', '大夫山']},
             '深圳': {'福田': ['莲花山', '赛格'],
                    '龙华': ['元山公园', '龙城广场'],
                    '南山': ['世界之窗', '欢乐谷']},
             '佛山': {'禅城': ['梁园', '孔庙'],
                    '南海': ['千灯湖', '南国桃园'],
                    '顺德': ['清晖园', '西山庙']}}

# 创建城市索引列表
city_index = [(index, key) for index, key in enumerate(city_dict)]
city_index.append((len(city_index), '退出'))  # 增加退出选项
while True:
	print('欢迎查询城市信息')
	print('--------------------------------')
	for i in city_index:  # 打印城市索引菜单
		for j in i:
			print(j, end=' ')
		print('')

	get_city = input('请选择查询的索引号：')
	if not get_city.isdigit():
		print('请输入一个数字索引号。')
		continue
	elif int(get_city) >= len(city_index):  # 输入索引号大于等于城市索引号长度
		print('输入的数字太大，请重输入。')
		continue
	elif int(get_city) == len(city_index) - 1:  # 最大的索引号为 退出程序对应的索引号
		print('欢迎再次登录，bye bye!')
		break
	else:
		choose_city = city_index[int(get_city)][1]  # 获取选择的城市名称
		# 创建 区 的索引列表
		area_index = [(index, key) for index, key in enumerate(city_dict[choose_city])]
		area_index.append((len(area_index), '返回'))  # 增加返回上一级菜单选项
		while True:
			for i in area_index:  # 打印选择城市的区索引菜单
				for j in i:
					print(j, end=' ')
				print('')

			get_area = input('请选择查询的索引号：')
			if not get_area.isdigit():
				print('请输入一个数字索引号。')
				continue
			elif int(get_area) >= len(area_index):  # 输入索引号大于城市索引号
				print('输入的数字太大，请重输入。')
				continue
			elif int(get_area) == len(area_index) - 1:  # 最大的索引号为 上级菜单对应的索引号
				print('返回到上一级菜单。')
				break
			else:
				choose_area = area_index[int(get_area)][1]  # 获取选择区的名称
				print(city_dict[choose_city][choose_area])  # 打印该区的信息
				print('--------------------------------')
'''

# def norm(name):
# 	return name.capitalize() #首字符大写
#
# L1 = ["adam","LISA","adDD"]
# L2 = list(map(norm,L1))
# print(L2)

# from functools import reduce
# i = 0
# def prod(L):
# 	def mycheng(x,y):
# 		return x*y
# 	return reduce(mycheng,L)  # 类似递归
# #	return reduce(lambda x,y:x*y,L)
# print("3*5*7*9 =",prod([3,5,7,9]))
# if prod([3,5,7,9]) == 3*5*7*9:
# 	print("ok")
# else:
# 	print("no")

#
# def f(i):
# 	if i == 1:
# 		return i
# 	return i * f(i-1)
# print(f(5))

# def fil(x):
# 	return x % 2 is 0
# print(list(filter(fil,range(10)))) # 10内的偶数
# l = []
# def huinum(n):
# 	for x in range(n):
# 		if str(x) == str(x)[::-1]: # 判断镜像数值
# 			l.insert(0,x)
# 	return l
# # print(list(filter(huinum,range(1000))))
# print(huinum(1000))
# l3 = 'abcdefghijklmnopqrstuvwsyz'
# print(l3[::-4]) # 倒置 步进长度

# list5 = ['1','2','3','4']
# print(list5[::-1])

# L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
# def by_name(t):
# 	return t[0].lower()
# L2 = sorted(L, key=by_name)
# print('姓名排序：%r'% L2)
#
# def by_name1(t):
# 	return t[1]
# L3 = sorted(L, key=by_name1,reverse=True)
# print('成绩排序：%r'% L3)

# from functools import reduce
# def calc_sum(*args):
# 	ax = 0
# 	for n in args:
# 		ax = ax + n
# 	return ax
# sum4 = calc_sum(1,2,3,4,5,6)
# print(sum4)

# def count():
# 	def f(x):
# 		def g():
# 			return x*x
# 		return g
# 	fs = []
# 	for i in range(1, 4):
# 		# def f():
# 		# 	return i*i
# 		fs.append(f(i))
# 		# print(fs)
# 	# for x in fs:
# 	# 	print(x())
# 	return fs
# f1, f2, f3 = count()
# print(f1(),f2(),f3())

# def createCounter():
# 	def func():
# 		n = 0
# 		while 1:
# 			n += 1
# 			yield n # 使用生成器 惰性，调用一次输出一次
# 	fun = func()
# 	def counter():
# 		return next(fun)
# 	return counter
#
# counterA = createCounter()
# print(counterA(), counterA(), counterA(), counterA(), counterA()) # 1 2 3 4 5
# counterB = createCounter()
# if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
#     print('测试通过!')
# else:
#     print('测试失败!')

# j = 0
# def func():
# 	global j
# 	j += 1
# 	print(j)
#
# func()

# set_1 = ([1,2,3],(4,5,6),{"key1":"val1","key2":"val2"})
# print(type(set_1))
# print(set_1[0][0])
# print(set_1[0][1])
# print(set_1[0][2])
# print(set_1[0])
# print(set_1[1][0])
# print(set_1[1][1])
# print(set_1[1][2])
# print(set_1[1])
# print(set_1[2]['key1'])
# print(set_1[2]['key2'])
# print(type(set_1[0]))

# str_1 = "hello word!"
# print(str_1[0:5])
# print(str_1[6:11])
# print(str_1[::-1])
# print(len(str_1))

# list_1 = ['hello','word!']
# print(list_1[0])
# print(list_1[0][0],list_1[0][1],list_1[0][2],list_1[0][3],list_1[0][4])
# print(list_1[1])
# print(list_1[1][0],list_1[1][1],list_1[1][2],list_1[1][3],list_1[1][4])
# print(list_1[::-1])

# tuple1 = ('hello','word!')
# tuple2 = ('abc')
# print(type(tuple2))
# tuple2 = ('abc',)
# print(type(tuple2))
# print(tuple1[0])
# print(tuple1[0][4])
# print(tuple1[1])
# print(tuple1[1][2])
# print(tuple1[::-1])

# dict1 = {"key1","val1",'102201',"people",'score',456}
# print(dict1)
# dict1 = ["a",'b','c','d','e','f']
# dict2 = [1,2,3,4,5,6]
# print(dict1.zip(dict2))
# print(dict1['key1'])
# print(dict1['102201'])
# print(dict1['score'])

# s1 = set([1, 1, 2, 2, 3,'wangye'])
# print(s1)
# s2 = set([2, 3, 4])
# print(s1 & s2) # 交集
# print(s1 | s2) # 并集


# test_1 = [[1,2,3],(4,5,6),{"key1":"val1","key2":"val2"}]
# strt = "字符串"
# print('测试常用格式化输出：字符串-》%s %s，整数-》%d，浮点数-》%.4f，十六进制-》%x'% (strt,'str',123,456,255))
# print('1: %s' % test_1)
# print('2:',test_1[0][0])
# print('3:',test_1[0][1])
# print('4:',test_1[0][2])
# print('5:',test_1[0])
# test_1[0] = set([7,8,9])
# print('6:',test_1[0])
# print('7:',test_1[1][0])
# print('8:',test_1[1][1])
# print('9:',test_1[1][2])
# print('10:',test_1[1])
# print('11:',test_1[2]['key1'])
# print('12:',test_1[2]['key2'])
# print('13:',test_1[2])

# arg = 123
# if isinstance(arg,int):
# 	print(type(arg))
# 	print("ok")
# else:
# 	print("no")


# d = {'a': 1, 'b': 2, 'c': 3}
# for key in d.values():
# 	print(key)
#
# l = [x*x for x in range(10)] # 列表解析
# print(l)
# j = (x*x for x in range(10)) # 生成器表达式    yield
# print(j)


# for i in range(10):
# 	j = True if i % 2 is 0 else False
# 	if j:
# 		print('ok')
# 	else:
# 		print("no")
# import os,datetime,time
# f = open('E:\\python_test\\test.txt','+a')
#
# for x in range(10):
# 	x = str(x)
# 	f.write('%s :\tabcd\tcedasd\n %s' % (x,time.strftime('%H:%M:%S')))
# f.close()

# fe = open('E:\\python_test\\test.txt')
# for j in fe.readlines():
# 	j = j.split()
# 	# print(list(j))
# 	if j[2] == 'abcd':
# 		print("ok")
# 	else:
# 		print("no")
# fe.close()

# def now():
# 	print('2018-04-13')
#
# f = now
# print(now.__name__)
# print(f.__name__)
# f()



# def newpos(m,n):
# 	print('new = %d %d' % (m+x,n+y))
# 	return m+x,n+y
# # return newpos
# x,y = 1,2
# print("old = %d %d"%(x,y))
# action = newpos(10,10)
# for i in action:
# 	print(i)


# def fun(n):
# 	i = 1
# 	while i <= n:
# 		yield i ** 2
# 		i += 1
# f1 = fun(10)
# for i in f1:
# 	print(i)

# def deco1(f1):
# 	def wp():
# 		print(1)
# 		f1()
# 	return wp
# def deco2(f2):
# 	def wp():
# 		print(2)
# 		f2()
# 	return wp

# i = 0
# def deco3(f3):
# 	def wp():
# 		f = open("E:\\python_test\\test.txt","a+")
# 		global i
# 		f.write("%d"% i)
# 		f.write("%s\n" % f3())
# 		f.close()
# 		i += 1
# 	return wp
# @deco3
# # @deco2
# # @deco1
# def showdoc():
# 	return "test"
# showdoc()

# def jiec(n):
# 	# print(type(n))
# 	if n >= 1:
# 		# print(n * jiec(n-1))
# 		return n * jiec(n-2)
# 	else:
# 		return 1
# print(jiec(5))

# class Student(object):
# 	def __init__(self,name,score):
# 		self.__name = name
# 		self.__score = score
# 	def get_grade(self):
# 		if self.__score >= 90 :
# 			# print('%s score grade is %s !' % (stu1.__name, 'A'))
# 			return 'A'
# 		elif self.__score >= 80 :
# 			return 'B'
# 		else:
# 			# return 'C'
# 			raise ValueError('YOU NO !') #自定义错误提醒
# 	def get_name(self):
# 		return self.__name
# 	def get_score(self):
# 		return self.__score
# name,score = input("Please input you name and  score:").split()
# stu1 = Student(name,int(score))
# # zhaomin = Student('zhaomin',89)
# # wangna = Student('wangna',69)
# # print("wangye grade is %s.zhaomin grade is %s.wangna grade is %s"%(wangye.get_grade(),zhaomin.get_grade(),wangna.get_grade()))
# print('%s score grade is %s ' %(name,stu1.get_grade()))
# # g_name = stu1.name()
# # g_score = stu1.score()
# print(stu1.get_name(),stu1.get_score())

# class Animal(object):
# 	def run(self):
# 		print('Animal is running')
# class Dog(Animal):
# 	def run(self):
# 		print('Dog is running')
# class Cat(Animal):
# 	def run(self):
# 		print('Cat is running')
# class nano(Animal):
# 	def test(self):
# 		pass
# def echo_class(x):
# 	x.run()
# a = Animal()
# b = Dog()
# c = Cat()
# f = nano()
# echo_class(a)
# echo_class(b)
# echo_class(c)
# echo_class(f)

# g = 'ABCDEFE'.lower()
# print(dir(g))
#
# print(help(list))
# print(g.capitalize())

# fd = open(r'E:\python_test\test.txt','r')
# if hasattr(fd,'read'):
# 	print("ok")
# else:
# 	print("no")

# import os
# def fn1():
# 	def fnn():
# 		print("hello fn1")
# 	return fnn
# def fn2():
# 	def fnnn():
# 		print("hello fn2")
# 	fnnn()
# a = fn1()
# b = fn2()
# print("---------")
# print(a)
# print(b)

# class Screen(object):
# 	@property               # 把类的方法变成实例的属性，隐藏变量
# 	def width(self):
# 		return self._width
# 	@width.setter
# 	def width(self, value):
# 		self._width = value
# 	@property
# 	def height(self):
# 		return self._height
# 	@height.setter
# 	def height(self,value):
# 		self._height = value
# 	@property        #只定义getter方法，不定义setter方法为只读属性
# 	def resolution(self):
# 		return self._width * self._height
#
# s = Screen()
# s.width = 1024
# s.height = 768
# print('resolution = ' ,s.resolution)
# if s.resolution == s.resolution:
# 	print('ok')
# else:
# 	print('no')

# class Student(object):
# 	def __init__(self,name):
# 		self.name = name
# 	def __str__(self):
# 		return "Student object (name:%s)" %self.name
# 	__repr__ = __str__
# print(Student("ABC"))
# s = Student("ddddddd")
# print(s)

# class Fib(object):
#     def __init__(self):
#         self.a, self.b = 0, 1 # 初始化两个计数器a，b
#
#     def __iter__(self):
#         return self # 实例本身就是迭代对象，故返回自己
#
#     def __next__(self):
#         self.a, self.b = self.b, self.a + self.b # 计算下一个值
#         if self.a > 1000: # 退出循环的条件
#             raise StopIteration()
#         return self.a # 返回下一个值
# for i in Fib():
# 	print(i)
# 	print('\t')

# class Fib(object):
# 	def __getitem__(self,value):#使用__getitem__方法可以像list按照元素下标来取出元素
# 		a,b = 0,1
# 		for x in range(value):
# 			a,b = b,a + b
# 		return a
# num = Fib()
# print(num[11])

# class Fib(object):
#     def __getitem__(self, n):
#         if isinstance(n, int): # n是索引,使用__getitem__方法取出索引值，如n为索引执行此if
#             a, b = 1, 1
#             for x in range(n):
#                 a, b = b, a + b
#             return a
#
#         if isinstance(n, slice): # n是切片,使用__getitem__方法取出切片，如果n为切片执行此if
#             start = n.start
#             print('切片初始位置：%s'% start)
#             stop = n.stop
#             print('切片结束位置：%d'% stop)
#             if start is None:
#                 start = 0
#             a, b = 1, 1
#             L = []
#             for x in range(stop):
#                 if x >= start:
#                     L.append(a)
#                 a, b = b, a + b
#             return L
#
# f = Fib()
# print('f 实例的第五个索引是：%s '% f[5])
# print(f[:8])

# class Student(object):
# 	def __init__(self):            # 初始属性
# 		self.name = 'Michael'
# 	def __getattr__(self, item):   # 动态属性
# 		if item == 'score':
# 			return 100
# 		elif item == 'age':
# 			return "man"
# 		raise AttributeError('you input error !')
# s = Student()
# print(s.name)
# print(s.score)
# print(s.age)
# print(s.abc)


# class Chain(object):
# 	def __init__(self,path=''):
# 		self._path = path
# 	def __getattr__(self, path):
# 		return Chain('%s/%s' %(self._path,path))
# 	def __str__(self):
# 		return self._path
# 	__repr__ = __str__
# s = Chain().users.michael.repos # 三个依次传参
# print(s)

# class Student(object):         # 使用__call__方法，使用实例本身调用实例方法
# 	def __init__(self,name):
# 		self._name = name
# 	def __call__(self, *args, **kwargs):
# 		# return 'hello world %s'% self._name
# 		for i in range(1,10):
# 			for j in range(1,i+1):
# 				print('%s * %s = %s\t' % (i,j,j*i),end='')
# 				if i == j:
# 					print('\n')
# 		return
# s = Student('wangye')
# print(s())

# from enum import Enum # 枚举
#
# Month = Enum('month',('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
# for name,member in Month.__members__.items():
# 	print(name,'=>',member,',',member.value)

# from enum import Enum
# class Gender(Enum):
# 	Male = 0
# 	Female = 1
# class Student(object):
# 	def __init__(self,name,gender):
# 		self.name = name
# 		self.gender = gender
# s = Student('wy',Gender.Male)
# if s.gender == Gender.Male:
# 	print('ok')
# else:
# 	print('no')

# import enum
# list1 = ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec')
# for i,j in enumerate(list1,1):#枚举型
# 	print('%s = %s '% (j,i))

# class Student(object):
# 	def __init__(self,name):
# 		self.name = name
# 	def __str__(self): # 返回指定字符串，可自定义类使用说明
# 		return "helo %s " % self.name
# 	def get_name(self):
# 		return self.name
# 	__repr__ = __str__
# s = Student('wangye')
# print(s)
# print(s.get_name())
# print('abc') if str(s.get_name()) == 'wangye'  else  print('ooo')

# import time
# ss = ['d','j','r']
# uu = ['wangye']
# print(ss.__add__(uu)) # 只是输出时添加uu内容，
# time.sleep(2)
# print(ss)

# import time
# from threading import Timer
#
# def func(a):
#     print(time.time(),"Hello Timer!",a)
# def fun2(a):
# 	print(time.time(),"Hello Timer 2 !",a)
#
# print('1 ',time.time())
# Timer(5,func,("test1",)).start() # timer 是异步执行  可用于多线程处理
# Timer(10,fun2,("test2",)).start() # threading 不需要把任务放在盒子里，直接start，因异步不分优先级，
# # s.start()
# # t.start()

# import sched,time
#
# def func(a):
#     print(time.time(),"Hello Sched!",a)
# def fun1(a):
# 	print(time.time(),"Hello Sched! sleep 1s",a)
# 	time.sleep(1)
# print(time.time())
# s = sched.scheduler(time.time,time.sleep)  # sched 类似阻塞执行，执行完成后再往下执行,   定时任务
# # 2为延后时间，1为优先级(0~****)，func为函数名，("test1",)为函数参数
# s.enter(2,2,func,("test1",))  # 延时时间都是2s，所以逻辑上是一起执行，但是0的优先级高，所以先执行fun1
# s.enter(2,0,fun1,("test2",))
# s.run()                       # 把enter任务放在run任务盒子里执行，没有run任务不会被执行
# print(time.time())
# print(s)

# try:                            # 预计有问题代码，放在try下执行
# 	print('try....')
# 	r = 10/5
# 	print('result:',r)
# except ZeroDivisionError as e:  # 可用多个except 判断错误类型，根据类型提示，
# 	print('except:',e)
# else:                           # 如果没有错误，可在后面加else 自动执行
# 	print('no error ')
# finally:                        # 上面代码执行完毕，执行finelly ，可有可无，有则一定会被执行
# 	print('finally...')
# print('end')

# import sys
# import mode                     # 导入自定义模块
# print(sys.path)
# t1=mode.mode('abc')             # 使用自定义模块
# print(t1)


# import logging
# logging.basicConfig(filename='new.log',filemode='a',format='%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s',level=logging.INFO)
# # name,number = input("Please input name and number !").split()
# name = '232'
# number = 9527
# if not isinstance(name,str):
# 	logging.info('name not is str %s',name)
# else:
# 	logging.info('name is str > %s ',name)
#
# if isinstance(number,int):
# 	logging.info('number is int type %d',number)
# else:
# 	logging.info('number not is int %d',number)

# data = 'abcdcef'
# for i in data.split('c',2):
# 	print(i)
















