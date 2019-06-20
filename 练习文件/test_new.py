
# # 初始化城市信息
# city_dict = {'广州': {'天河': ['天河体育馆', '金山大夏'],
#                     '越秀': ['越秀公园', '光孝寺'],
#                     '番禺': ['长隆欢乐世界', '大夫山']},
#              '深圳': {'福田': ['莲花山', '赛格'],
#                     '龙华': ['元山公园', '龙城广场'],
#                     '南山': ['世界之窗', '欢乐谷']},
#              '佛山': {'禅城': ['梁园', '孔庙'],
#                     '南海': ['千灯湖', '南国桃园'],
#                     '顺德': ['清晖园', '西山庙']}}
#
# # 创建城市索引列表
# city_index = [(index, key) for index, key in enumerate(city_dict)]
# city_index.append((len(city_index), '退出'))  # 增加退出选项
# while True:
# 	print('欢迎查询城市信息')
# 	print('--------------------------------')
# 	for i in city_index:  # 打印城市索引菜单
# 		for j in i:
# 			print(j, end=' ')
# 		print('')
#
# 	get_city = input('请选择查询的索引号：')
# 	if not get_city.isdigit():
# 		print('请输入一个数字索引号。')
# 		continue
# 	elif int(get_city) >= len(city_index):  # 输入索引号大于等于城市索引号长度
# 		print('输入的数字太大，请重输入。')
# 		continue
# 	elif int(get_city) == len(city_index) - 1:  # 最大的索引号为 退出程序对应的索引号
# 		print('欢迎再次登录，bye bye!')
# 		break
# 	else:
# 		choose_city = city_index[int(get_city)][1]  # 获取选择的城市名称
# 		# 创建 区 的索引列表
# 		area_index = [(index, key) for index, key in enumerate(city_dict[choose_city])]
# 		area_index.append((len(area_index), '返回'))  # 增加返回上一级菜单选项
# 		while True:
# 			for i in area_index:  # 打印选择城市的区索引菜单
# 				for j in i:
# 					print(j, end=' ')
# 				print('')
#
# 			get_area = input('请选择查询的索引号：')
# 			if not get_area.isdigit():
# 				print('请输入一个数字索引号。')
# 				continue
# 			elif int(get_area) >= len(area_index):  # 输入索引号大于城市索引号
# 				print('输入的数字太大，请重输入。')
# 				continue
# 			elif int(get_area) == len(area_index) - 1:  # 最大的索引号为 上级菜单对应的索引号
# 				print('返回到上一级菜单。')
# 				break
# 			else:
# 				choose_area = area_index[int(get_area)][1]  # 获取选择区的名称
# 				print(city_dict[choose_city][choose_area])  # 打印该区的信息
# 				print('--------------------------------')


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


# import inspect
#
# def test_fn(fn):
# 	parms = inspect.signature(fn) # 获取fn()所有参数
# 	parms_s = parms.parameters # 返回参数是有序字典类型及参数
# 	# print(parms,parms_s)
# 	for name,parm in parms_s.items():
# 		# print('name:',name,'parm:',parm)
# 		if parm.kind == inspect.Parameter.KEYWORD_ONLY: # 判断fn()参数最后参数是否是关键字参数
# 			print(parm,'is keyword_only')
#
# def funt(r, p=88,b=0, *c, g,i,d, e=1,x, **f):
# 	pass
# test_fn(funt)



# 位置参数 : test(m,n) 传参时一定要传两个参数，m、n各分配一个
# 默认参数 ： test（m,n=3) 传参时只需传一个参数，分配给m
# 可变参数 ： test(*args) 可传任意个参数，以元组方式调用,args.number
# 关键字参数 ： test(**kwargs) 可传递任意个参数，以字典方式调用，传参时使用K=V格式,调用时kwargs['k']
# 命名关键字参数 ：test(m,n,*ar,x,y) 传参时带*参数后的参数要以K=V格式，数量对应
# 注意：
# 混用时参数定义的顺序必须是：位置参数–>默认参数–>可变参数–>命名关键字参数–>关键字参数

# def person(name, age, *args, city, job):
#     print(name, age, args, city, job)
#
# person('wy',18,'args',job='it',city='bj')

# inspect模块：inspect.Parameter.*** 对比 parms.kind的类型
# POSITIONAL_ONLY        位置参数
# POSITIONAL_OR_KEYWORD	 位置参数或关键字参数
# VAR_POSITIONAL	     可变参数（*args）
# KEYWORD_ONLY	         命名关键字参数
# VAR_KEYWORD	         关键字参数

# import random
# r = random.randint(65,90)
# print(r)
# print(chr(r))

# from urllib.request import urlopen
# for line in urlopen('http://www.baidu.com'):
# 	line = line.decode('utf-8') # Decoding the binary data to text.
# 	print(line)

# from datetime import date
# now = date.today()
# # print(now)
# # now = now.strftime('''
# # 					%m-%d,
# # 					%D,
# # 					%Y,
# # 					''')
# # print(now)
# n, y, r = input('请输入你的出生年月：').split()
# birthday = date(int(n),int(y),int(r))
# age = now - birthday
# age = age.days//365
# print('您的年龄为：', age)

# import logging,os,datetime
# import logging.handlers
# # os.makedirs('log\\loging.txt')
# i = 0
# if os.path.isfile('log\\loging.txt'):
# 	logfile = 'log\\loging.txt'
# else:
# 	if not os.path.isdir('log'):
# 		os.mkdir('log')
# 	f = open('log\\loging.txt', 'w')
# 	f.close()
# 	logfile = 'log\\loging.txt'
# # logging.basicConfig(filename=logfile, filemode='a', level=logging.DEBUG)
# my_logger = logging.getLogger('loging.txt')
# my_logger.setLevel(logging.DEBUG)
# head = logging.handlers.RotatingFileHandler(logfile, maxBytes=5128, backupCount=5)
# my_logger.addHandler(head)
#
# for item in list(range(10)):
# 	my_logger.debug('%s:这是第%s条日志' % (datetime.date.today(), item))
# 	my_logger.warning('warning messages!')

# import weakref,gc
#
# class A:
# 	def __init__(self,value):
# 		self.value = value
# 	def __repr__(self):
# 		return str(self.value)
# a = A(10)
# # d = weakref.WeakValueDictionary()
# d = {}
# d['pri'] = a
# print(d['pri'])
# del a
# # print(gc.collect())
# print(d['pri'])

# print('{},{}'.format('a','b'))
# print('{1},{0}'.format('A', 'B'))
# print('{arg1},{arg2}'.format(arg2='AA', arg1='BB'))


# import json
# ret = json.dumps([1,'eee', 'ppp']) # 序列化，转字符串
# print(type(ret),' : ', ret,' : ', ret[::-1])
#
# with open('test.txt', 'w') as f:
# 	json.dump([1,'eee', 'ppp'], f) # 存入文件
# with open('test.txt', 'r') as f:
# 	result = json.load(f) # 文件读出数据
# 	print(result)
#
# unret = json.loads(ret) # 反序列化，反转字符串
# print(type(unret), unret)


# import re
#
# data = 'ao fn av osi dfjawnv https://www.baidu.com zkndvo answww.sohu.netd eifasdn'
# re = re.findall('www.\w+.\w{3}', data)
# if re is not None:
# 	print(re)
#
# print(data.replace('osi','wangye'))


# from socket import *

# import random
# l = [1,3,5,'g','e','g']
# d = {'name1':'v1',
#      'name2':'v2',
#      'name3':'v3',
#      'name4':'v4',
# 	 'name5':'v5',
#      'name6':'v6',
#      'name7':'v7',
#      'name8':'v8'
#      }
# l1 = list(d.keys())
# print(random.random())
# print(random.randint(1,100))
# name = random.choice(l1)
# print(name)
# print(d[name])
# print(random.sample(l1)
# print(random.randrange(0,100,2))
# print(random.uniform(0, 360))

# class diff():
# 	def __init__(self, a1, a2):
# 		self.a1 = a1
# 		self.a2 = a2
# 	def __str__(self):
# 		result = set(self.a1) ^ set(self.a2)
# 		return str(result)
#
# from random import shuffle,sample
# import random
# # print(shuffle.__doc__)
# ret = []
# res1 = []
# res2 = []
# res3 = []
# res4 = []
# values = ['2','3','4','5','6','7','8','9','10','j','q','k','a']
# suits = '黑花 红桃 方片 红花'.split()
# for i in values:
# 	for j in suits:
# 		ret.append(j+i)
# for i in range(1,14):
# 	result = random.choice(ret)
# 	res1.append(result)
# 	ret.remove(result)
# print('1:',res1, sep='\r\n')
# for i in range(1,14):
# 	result = random.choice(ret)
# 	res2.append(result)
# 	ret.remove(result)
# print('2:',res2, sep='\r\n')
# for i in range(1,14):
# 	result = random.choice(ret)
# 	res3.append(result)
# 	ret.remove(result)
# print('3:',sorted(res3), sep='\r\n')
# for i in range(1,14):
# 	result = random.choice(ret)
# 	res4.append(result)
# 	ret.remove(result)
# print('4:',res4, sep='\r\n')
# print(ret)
# # random.shuffle(ret)
# # print(ret)
# # shou = sample(ret, 12)
# # print('第一人：', shou)
# # ret = diff(ret, shou)
# # print(ret)
# # # shou = sample(ret, 12)
# # # print('第二人：', shou)
# # # ret = diff(ret, shou)
# # # shou = sample(ret, 12)
# # # print('第三人：', shou)
# # # ret = diff(ret, shou)
# # # shou = sample(ret, 12)
# # # print('第四人：', shou)

# from time import time, sleep
# import threading
# def loop0():
# 	print('start loop0')
# 	sleep(4)
# 	print('stop loop0')
#
# def loop1():
# 	print('start loop1')
# 	sleep(2) # 阻塞 操作
# 	print('stop loop1')
#
# def main():
# 	print('start ....')
# 	T1 = threading.Thread(target=loop0, daemon=False)
# 	T2 = threading.Thread(target=loop1, daemon=False)
# 	T1.start()
# 	T2.start()
# 	T1.join() # 阻塞，执行完线程才继续执行
# 	T2.join()
# 	sleep(6)
# 	print('close')
# if __name__ == '__main__':
# 	main()




# import threading
# from time import sleep
#
# loops = [4, 2]
#
# class ThreadF(object):
# 	def __init__(self, func, args, name=''):
# 		self.name = name
# 		self.func = func
# 		self.args = args
# 	def __call__(self):
# 		self.func(*self.args)
#
# def loop(nloop, nsec):
# 	print('start loop fun ', nloop)
# 	sleep(nsec)
# 	print('stop loop fun ', nloop)
#
# def main():
# 	print('start main ..')
# 	threads = []
# 	nloops = range(len(loops))
# 	for i in nloops:
# 		# t = threading.Thread(target=loop, args=(i, loops[i]))
# 		t = threading.Thread(target=ThreadF(loop, (i, loops[i]), loop.__name__))
# 		threads.append(t)
# 	for i in nloops:
# 		threads[i].start()
# 	for i in nloops:
# 		threads[i].join() # 等待线程结束才继续往下执行
# 	print('stop main ...')
# if __name__ == '__main__':
# 	main()

# import threading
# from time import sleep
#
# class ThreadF(threading.Thread):
# 	def __init__(self, func, args):
# 		threading.Thread.__init__(self) # 必须调用基类的构造函数
# 		self.func = func
# 		self.args = args
# 		self.res = ''
# 	def getresult(self):
# 		return self.res
# 	def run(self):
# 		self.res = self.func(*self.args)
# 		# print(self.res)
#
# def fib(x):
# 	sleep(0.05)
# 	if x < 2:return 1
# 	return (fib(x-2) + fib(x-1))
#
# def fac(x):
# 	sleep(0.05)
# 	if x < 2 :return 1
# 	return (x * fac(x -1))
#
# def sum(x):
# 	sleep(0.05)
# 	if x < 2 :return 1
# 	return (x + sum(x-1))
#
# funcs = [fib, fac, sum]
# n = 12
# def main():
# 	print('start main ..')
# 	threads = []
# 	nloops = range(len(funcs))
# 	for i in nloops:
# 		# t = threading.Thread(target=loop, args=(i, loops[i]))
# 		# t = ThreadF(loop, (i, loops[i]), loop.__name__)
# 		t = ThreadF(funcs[i], (n,))
# 		threads.append(t)
# 	for i in nloops:
# 		threads[i].start()
# 	for i in nloops:
# 		threads[i].join() # 等待线程结束才继续往下执行
# 		print(threads[i].getresult()) # 输出三个函数的结果
# 	print('stop main ...')
# if __name__ == '__main__':
# 	main()


# l = []
# a = 0
# b = 1
# for i in range(0, 12):
# 	a,b = a+b,a
# 	l.append(a)
# print(l)


# from atexit import register
# from re import compile
# from threading import Thread
# from time import ctime
# from urllib.request import urlopen
#
# REGEX = compile(r'\bappKey.*')
# AMZN = 'https://www.csdn.net/'
# def main():
# 	data = urlopen(AMZN)
# 	data1 = data.read()
# 	reg = data1.decode('utf-8')
# 	RES = REGEX.findall(reg)
# 	print(RES)
# 	data.close()
#
# @register # 退出程序前执行，不需调用
# def _eee():
# 	print('end ....')
#
# if __name__ == '__main__':
# 	main()


# import random
# loops = (random.randint(2, 5) for x in range(random.randint(3, 7)))
#
# for i in loops:
# 	print(i)

# import threading
# import time
#
# def run():
#     time.sleep(1)
#     print('当前线程的名字是： ', threading.current_thread().name)
#     time.sleep(1)
#
# if __name__ == '__main__':
#     start_time = time.time()
#     # print(start_time)
#     print('这是主线程：', threading.current_thread().name)
#     thread_list = []
#     for i in range(5):
#         t = threading.Thread(target=run)
#         thread_list.append(t)
#     for t in thread_list:
#         t.setDaemon(False) # True时，主线程结束，子线程全部结束， False时，主线程结束后，子线程执行到程序终止
#         t.start()
#         t.join() # 主线程结束后阻塞，直至所有子线程结束后退出，执行后面代码
#     print('主线程结束！' , threading.current_thread().name)
#     # print(time.time())
#     print('一共用时：', time.time()-start_time)

# from concurrent.futures import ThreadPoolExecutor # 方法：'map', 'shutdown', 'submit'
# from re import compile
# from time import ctime
# from urllib.request import urlopen as uopen
#
#
# REGEX = compile(b'#([\d,]+) in Books ')
# AMZN = 'https://www.amazon.cn/gp/bestsellers/books/'
# ISBNs = {
# 	''
# }

# print(dir(ThreadPoolExecutor))


# import threading,time
#
# def run(n):
#     semaphore.acquire()
#     time.sleep(1)
#     print("run the thread: {}, sec: {}".format(n,time.time()))
#     semaphore.release()
#
# if __name__ == '__main__':
#     stime = time.time()
#     semaphore  = threading.BoundedSemaphore(5) #最多允许5个线程同时运行
#     for i in range(7):
#         t = threading.Thread(target=run,args=(i,))
#         t.start()
#         # t.join() # 等待子线程执行完毕才可继续执行，是多线程无意义
#
# while threading.active_count() != 1:
#     pass #print threading.active_count()
# else:
#     print('----all threads done---')
#     print('total time : {}'.format(time.time() - stime))


# import tkinter
#
# top = tkinter.Tk()
# label = tkinter.Label(top, text='你好')
# button = tkinter.Button(top, text='shuit ', command=top.quit, bg='red', fg='white')
# button.pack(fill=tkinter.X, expand=1)
# label.pack()
# tkinter.mainloop()


# from tkinter import *
#
# def resize(ev=None):
# 	label.config(font='Helvetica -%d bold' % scale.get())
#
# top = Tk()
# top.geometry('250x150')
# label = Label(top, text='hello world! ', font='Helvetica -12 bold')
# label.pack(fill=Y, expand=1)
# scale = Scale(top, from_=0, to=100, orient=HORIZONTAL, command=resize, activebackground='blue')
# scale.set(20)
# scale.pack(fill=X, expand=1)
# quit = Button(top, text='exit', command=top.quit, activeforeground='white',activebackground='red')
# quit.pack()
# mainloop()


# # 模仿栈，类实现后进先出结构
# class FooStack(object):
# 	def __init__(self):
# 		self.stack = []
# 	def push(self, value):
# 		self.stack.append(value)
# 	def pop(self):
# 		return self.stack.pop() # 默认移除索引最大的值
# 	def res(self):
# 		return self.stack
#
# a = FooStack()
# a.push('1-value')
# a.push('2-value')
# print(a.res())
# print(a.pop())
# print(a.res())

# import sys, os
# # print(sys.path)
# Path_file_name = os.path.abspath(__file__)
# print(Path_file_name)
# Path_file_dir = os.path.dirname(os.path.abspath(__file__))
# print(Path_file_dir)
# print(__file__)
#
# if sys.argv[1]:
# 	with open(sys.argv[1]) as f:
# 		for i in f.readlines():
# 			print(i)
# else:
# 	print('not stdin')

# import sys
# print(sys.platform)
# listt = ['a', 'b', 'c']
# listt.reverse()
# print(listt)


# import webbrowser
# webbrowser.open('www.baidu.com')


# import heapq
# from random import shuffle
#
# heap = []
# for i in range(10):
# 	heapq.heappush(heap, i)
# shuffle(heap)
# print(heap)
# for i in range(5):
# 	heapq.heappop(heap)
# print(heap)


# a, b = 0, 1
# while b < 100:
# 	a, b = a+b, a
# 	print(a)

# str1 = '1234'
# # list1 = [1,2,3,4]
# # for i in reversed(list1):
# # 	print(i)
# for i in range(len(str1)-1,-1,-1):
# 	print(str1[i])

# ls = [1,1,1,1,14,4,5,5,6,6,7]
# # print(list(set(ls)))
# d = {}
# for i in ls:
# 	d[i] = 1
# print(list(d.keys()))

# import copy
#
# a = ['1', '4']
# print(id(a))
# b = copy.copy(a)
# print(id(b))
# c = copy.deepcopy(a)
# print(id(c))


# str1 = 'wo shi wangye de hao pengyou '
# str2 = str1.replace('de', '666')
# print(str2,id(str1),id(str2))

# html = '''
# 		<input>sadfasdfasdf</input>
# 		<input>123123123123123</input>
# '''
# import re
# res = re.findall(r'<\w{5}>\w+</\w{5}>', html)
# print(res)

# import random
# ll = ['1','2','3', '13','32','33']
# print(random.random())
# print(random.randint(99, 111))
# print(random.choice(ll))
# random.shuffle(ll) # 没有输出和return
# print(ll)
# print(random.sample(ll, 3))


# import shutil
#
# shutil.copyfile('new.log','copytest.log')

# lls = [1,3,5,7,9]
# lls1 = [8,3,4,2,1]
# jiao = [i for i in lls if i in lls1]
# print(jiao)
# cha = [i for i in lls if i not in lls1]
# cha1 = [i for i in lls1 if i not in lls]
# print(cha, cha1)

# src = "security/afafsff/?ip=123.4.56.78&id=45"
# import re
# result = re.findall(r'(?:\d{1,3}\.){3}\d{1,3}', src)
# print(result)


# data = {"persons":[{"name":"yu","age":"23"},{"name":"zhang","age":"34"}]}
# print(data['persons'][0]['name'])

# # 平衡点，某一元素前后值得和相同
# num = [1,3,5,7,8,5,5,25,4,20,10]
# total = sum(num)
# fore = 0
# for i in num:
# 		if fore == (total-i)/2:
# 			print(i)
# 			exit(0)
# 		else:
# 			fore+=i
# print('not found!')

# # 支配点
# li = [4,4,1,2,4]
# cont = len(li)
# sot = []
# indx = []
# j = 0
# for i in range(cont):
# 	sot.append(li.count(li[i]))
# max_count = sorted(sot, reverse=True)[0]
# if max_count > cont/2:
# 	for k in sot:
# 		if k == max_count:
# 			indx.append(j)
# 		j+=1
# 	print('\033[1;31m支配数是{}，支配点是{}\033[0m'.format(li[0], indx))
# else:
# 	print('not have! ')

# str1 = ' asdf '
# print(str1.islower())

# a, b = 3, 7
# print(b//a)
# print(b%a)
# print(b**a)

# print(0b01001 | 0b11010)

# # 元组拆包可以应用到任何迭代对象上，
# # 唯一的要求是， 被可迭代对象中的元素数量必须要和这些元素的元组的空档数一致，
# # 除非我们用* 来表示忽略多余的元素。
# import os
# path, fnam = os.path.split('/ad/afd/vd/qwer/filename')
# print(path, fnam)
# tuple1 = ('cab', 'cad', 'uuu')
# a, b, c= tuple1
# print(a,b,c)
# tuple2 = ('cab', 'cad', 'uuu')
# a, *b= tuple2 # 使用*处理剩下的元素
# print(a,b)

# ls1 = [x*2 for x in range(5)] # 列表解析式
# print(ls1)
# ls2 = (x*2 for x in range(5)) # 生成器表达式，比列表解析节省内存
# print(ls2)
# print(list(map(lambda x: x*2, range(5))))

# l1 = ['a','d']
# l2 = ['r', 't']
# l1.extend(l2)
# print(l1, l2)

# def fun2(fun):
# 	def wrapper(ar):
# 		print('start fun2 ')
# 		fun(ar)
# 		print('end fun2')
# 	return wrapper
# @fun2
# def fun1(x):
# 	print('start fun1  ' + x)
#
# fun1('args ')

# import urllib.request
# print(help(urllib.request))


# import urllib
# import urllib.request
# import re
#
# def download_page(url):
#     request = urllib.request.Request(url)
#     response = urllib.request.urlopen(request)
#     data = response.read()
#     return data
# def get_image(html):
#     regx = r'https://[\S]*\.jpg'
#     pattern = re.compile(regx)
#     get_image = re.findall(pattern,repr(html))
#     num = 0
#     for img in get_image:
#         image = download_page(img)
#         with open('D:\image\%s.jpg'%num,'wb') as fp:
#             fp.write(image)
#             num += 1
#             print('正在下载第%s张图片'%num)
#     return
#
# url = 'https://www.biquge5200.cc/'
# print('正在爬取')
# html = download_page(url)
# get_image(html)

# # 冒泡排序
# temp = 0
# list1 = [4, 2, 1, 5, 9, 7]
# def bubble_sort(ls):
# 	for i in range(len(ls)-1):
# 		for j in range(len(ls)-i-1):
# 			if ls[j] < ls[j+1]:
# 				ls[j], ls[j+1] = ls[j+1], ls[j]
# 				# 下面是C 方法， 代码冗余
# 				# temp = ls[j]
# 				# ls[j] = ls[j+1]
# 				# ls[j+1] = temp
# 	return ls
# res = bubble_sort(list1)
# print(res)


# def demo(arg1,*args,**kwargs):
# 	print('arg1:{ar}'.format(ar=arg1))
# 	for x in args:
# 		print('args :{args}'.format(args=x))
# 		print('kwargs :{}'.format(kwargs['ks']))
# demo('a', 'b', 'c', 'd', kw='abcd',ks='name')

# # 两个列表合并排序，去重
# list1 = [1, 4, 6, 8, 2, 3]
# list2 = [5, 7, 8, 2, 4, 3]
# # for i in list1:
# # 	list2.append(i)
# list2.extend(list1)
# for i in range(len(list2)-1):
# 	for j in range(len(list2)-i-1):
# 		if list2[j] > list2[j+1]:
# 			list2[j], list2[j+1] = list2[j+1], list2[j]
#
# list3 = list(set(list2))
# print(list3)

# # 反转字符串
# def transtr(str):
# 	arg = str[::-1]
# 	print(arg)
# transtr('abcdef')
# print(list(reversed('abcdef')))


# l1 = [1, 3, 5]
# if type(l1) is list: # tpye() 不能判断子类和父类的关系
# 	print('list')
# if isinstance(l1, list):
# 	print('isinstance list')

# print([x for x in range(1,21) if x > 10])

#!/usr/bin/env python

# import os
# import sys
#
# def dirfun(darg):
#     dir_list = os.listdir(darg)
#     for i in dir_list:
#         child = os.path.join(darg, i)
#         if os.path.isdir(child):
#             dirfun(child)
#         elif os.path.isfile(child):
#             print('file : ',child)
# dirfun('D:\\12306Bypass\\')


# # 单实例,
# class testC(object):
# 	_instance = None
# 	def __new__(cls, *args, **kwargs):
# 		if not cls._instance:
# 			cls._instance = super(testC, cls).__new__(cls, *args, **kwargs)
# 		return cls._instance
#
# a = testC()
# b = testC()
# print(id(a), id(b))


# print('   str   '.lstrip())
# print('   str   '.rstrip())
# print('   str   '.strip())


# import datetime,time
# print(datetime.datetime.today())
# print(datetime.datetime.now())
# print(time.time())


# import copy
# a = ['a', [1,2,3], 'c']
#
# print(id(a))
# print(id(a[1]))
# print(id(a[1][1]))
# print(id(a[0]))
# b = copy.copy(a)
# print('----浅拷贝后:b-----')
# print(id(b))
# print(id(b[1]))
# print(id(b[1][1]))
# print(id(b[0]))
# c = copy.deepcopy(a)
# print('----深拷贝后:c-----')
# print(id(c))
# print(id(c[1]))
# print(id(c[1][1]))
# print(id(c[0]))


# a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# # b = [x for x in a if x % 2 != 0]
# # print(b)
# b = filter(lambda x:x%2!=0, a)
# print(list(b))

# # 嵌入元组排序，排序按照元组第二列降序排列，如相等按第三列排列
# students = [('john', 'A', 15, 9), ('jane', 'B', 12, 8), ('dave', 'B', 10, 1), ('dave', 'B', 10, 2)]
# print(sorted(students,key=lambda a:(a[1], a[3]), reverse=True))

# strtest = ['asdfc','qwe', 'opoiopi','as']
# print(sorted(strtest, key=lambda le:len(le)))

# foo = [-5,8,0,4,9,-4,-20,-2,8,2,-4]
# print(sorted(foo, key=lambda i:(i<0, abs(i)))) # 先按正数小到大，负数大到小


# import datetime
# print('data:{},week:{}'.format(str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')),
#                                str(datetime.datetime.now().isoweekday())))

# import random
# print(random.randint(1,100))
# print(random.choice(range(1, 101)))
# print(100*random.random())

# import re
# s='info:xiaoZhang 33 shandong'
# print(re.split(r':| ', s))
# print(s.split(':'),s.split(':')[1].split(' '))

# 去重排序
# s = "ajldjlajfdljfddd"
# b = list(set(s))
# b.sort() # 排序，没有返回新数据
# print(''.join(b))

# a = b'hello'
# b = '时间'
# print(a, b.encode(encoding='utf-8')) # 编字节

# a = [1, 3, 2]
# b = ['e', 'p']
# a.extend(b)
# print(a)
# print(a+b)

# def tfun():
# 	for x in range(1,10):
# 		yield x
# a = tfun()
# print(a.__next__)

# with open('new.log' ) as f:
# 	for l in f.readlines():
# 		print(l)

# 大文件读取
# with open('new.log') as f:
#     for line in f:
#         print(line)

# from django.shortcuts import HttpResponse,render, redirect

# s = '<div class="nam">中国</div>'
# import re
# res = re.findall(r'<div class=".*">(.*)</div>', s)
# print(res)

# # 断言
# def fun(arg):
# 	res = arg ** 2
# 	assert(res<82) # 括号内表达式成立，则继续执行，反之报错
# 	print(res)
#
# fun(10)

# a = '78'
# b = '78'
# print(id(a), id(b))
# a = '12'
# print(a[0])
# c = '78'
# print(id(c))
# # a = ['7', '8']
# # b = ['7', '8']
# # print(id(a), id(b))


# s = 'ajldjlajfdljfddd'
# s = list(set(s))
# s.sort()
# print(''.join(s))


# dict={"name":"zs","age":18,"city":"深圳","tel":"1362626627"}
# list = sorted(dict.items(), key=lambda x:(x[0]), reverse=False)
# print(list)
# new_d = {}
# for i in list:
# 	new_d[i[0]] = i[1]
# print(new_d)

# from collections import Counter
# str1 = 'kjalfj;ldsjafl;hdsllfdhg;lahfbl;hl;ahlf;h'
# cot = Counter(str1)
# print(cot)

# 先切成列表，在对列表每个元素过滤，再转成字符串
# import re
# a = "not 404 5.99 found 张三 99 深圳"
# list1 = a.split()
# new_l = []
# patton = re.compile(r'(\d+\.?\d*|[a-zA-Z]+)')
# for i in list1:
# 	res = patton.findall(i)
# 	print(res)
# 	if not res:
# 		new_l.append(i)
# print(' '.join(new_l))

# a =  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# new_a = filter(lambda x:x % 2 != 0, a)
# print(list(new_a))


# import datetime
# print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),'week:', datetime.datetime.now().isoweekday())

# # 一行代码解析，取出单个元素列表进行弹出处理
# print([j for i in [[1,2],[3,4],[5,6]] for j in i])

# # x="abc",y="def",z=["d","e","f"],分别求出x.join(y)和x.join(z)返回的结果
# x = 'abc'
# y = 'def'
# z = ['d', 'e', 'f']
# print(x.join(y), x.join(z))


# # a="张明 98分"，用re.sub，将98替换为100, 两种方法
# import re
# a = '张明 98分'
# b = re.sub(pattern='\d{2}', repl='100', string=a)
# c = a.replace('98', '100')
# print(c, b)

# 不用sort排序，使用冒泡
# list=[2,3,5,4,9,6]
# for i in range(len(list)-1):
# 	for j in range(len(list)-i-1):
# 		if list[j] > list[j+1]:
# 			list[j], list[j+1] = list[j+1], list[j]
# print(list)

# # 使用round保留两位小数
# a="%.03f"%1.3335
# print(a)
# print(round(float(a), 2))


# s = 'asdf.effe:daef wiiu'
# import re
# print(re.split(r'\.|:| ', s))

# # 两种方式反转元素
# tempList = [1,2,3,4]
# # tempList.reverse()
# print(tempList)
# for i in range(len(tempList)-1,-1,-1):
# 	print(tempList[i])

# print(list(range(5,-1,-1))) # 反序输出[5, 4, 3, 2, 1, 0]

# # 如何查询和替换一个文本中的字符串, 两种方法
# str1 = 'hello bj to china !'
# str2 = str1.replace('bj', 'hangkang')
# print(str2)
# import re
# print(re.sub(pattern='bj', repl='dongbei', string=str1))

# # 使用python实现单例模式
# # 在__new__方法中把类实例绑定到类变量_instance上，如果cls._instance为None表示该类还没有实例化过，
# # 实例化该类并返回。如果cls_instance不为None表示该类已实例化，直接返回cls_instance
# class sig(object):
# 	_instance = None
# 	def __new__(cls, *args, **kwargs):
# 		if not cls._instance:
# 			cls._instance = super(sig, cls).__new__(cls, *args, **kwargs)
# 		return cls._instance


# # 闭包 ,装饰器就是一种闭包
# def func(arg):
# 	def sumfun(arg):
# 		return arg**2
# 	return sumfun(arg)
#
# a = func(5)
# print(a)

# # 装饰器
# def fun(arg): # arg = tset:被装饰的函数,
# 	def wrapper(s): # s = a：被装饰的函数参数
# 		print('start...')
# 		arg(s)
# 		print('end')
# 	return wrapper
#
# @fun
# def tset(a):
# 	print('tset')
# 	return a**2
#
# tset(5)

# # alist [{“name”:”a”,”age”:20},{“name”:”b”,”age”:30},{“name”:”c”,”age”:25}]按照 age 从大到小排序
# alist = [{'name':'a', 'age':20}, {'name':'b', 'age':29},{'name':'a', 'age':18}]
# blist = sorted(alist, key=lambda x:x['age'])
# print(blist)


# # 用简洁的方法合并alist = [‘a’,’b’,’c’,’d’,’e’,’f’]
# # blist = [‘x’,’y’,’z’,’e’,’f’]并且元素不能重复
# alist = ['a', 'b', 'c', 'd', 'e', 'f']
# blist = ['w', 'e', 'c', 'r', 'e', 'p']
# alist.extend(blist)
# print(list(set(alist)))

# alist = ['a','b','c','d','e','f']
# blist = ['x','y','z','e','f']
# def merge_list(*args):
#     s = set()
#     for i in args:
#         print(i)
#         s = s.union(i) # union 合并集合，并去除重复元素
#     print(s)
#     return s
# merge_list(alist,blist)

# # 序列随机排序
# from random import shuffle
# list1 = [1,2,3,4,5,6,7,8,9]
# shuffle(list1)
# print(list1)
#
# import random
# list1 = [1,2,3,4,5,6,7,8,9]
# list2 = []
# for i in range(len(list1)):
# 	j = random.choice(list1)
# 	list2.append(j)
# 	list1.remove(j)
# print(list2)

# # 简单实现栈结构，stack， 先进后出，队列是先进先出
# class Stack(object):
#     def __init__(self):
#         self.value = []
#     def push(self,x):
#         self.value.append(x)
#     def pop(self):
#         self.value.pop()
# stack = Stack()
# stack.push(1)
# stack.push(2)
# stack.push(3)
# print(stack.value)
# stack.pop()
# print(stack.value)
# class Queue(object):
#     def __init__(self):
#         self.value = []
#     def push(self,x):
#         self.value.insert(0, x)
#     def pop(self):
#         self.value.pop()
# queue = Queue()
# queue.push(1)
# queue.push(2)
# queue.push(3)
# print(queue.value)
# queue.pop()
# print(queue.value)

# # # 根据日志返回一年第几天
# from datetime import datetime
# def which_day(year,month,day):
#     return (datetime(year,month,day)-datetime(year,1,1)).days+1
#
# print(which_day(2017,10,18))

# # 把字符串”k1:1|k2:2|k3:3”处理成 python 字典的形式:{k1:1,k2:2,k3:3}
# str1 = 'k1:1|k2:2|k3:3'
# # import re
# # list1 = re.split(r':|\|', str1)
# # dict1 = {}
# # for i in range(len(list1)):
# # 	if i % 2 == 0:
# # 		dict1[list1[i]] = int(list1[i+1])
# # print(dict1)

# d = {}
# for kv in str1.split('|'):
# 	k, v = kv.split(':')
# 	if v.isdigit(): # 判断v值是否是是数字
# 		v = int(v)
# 	d[k] = v
# print(d)
# print('234'.isdigit())

# # 判断输入的值是否在二维数组中
# arr = [[1,4,7,10,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
# def fun(num):
# 	for i in arr:
# 		if num in i:
# 			return True
# 		else:
# 			return False
#
# ind = int(input('Please number :'))
# res = fun(ind)
# print(res)

# # 最大公约数
# a= 16
# b=12
# def max_common(a,b):
#     while b:
#         a,b=b,a%b
#     return a
# i = max_common(a, b)
# print(i)



# # 创建两个线程，其中一个输出1-52，另外一个输出A-Z。输出格式要求：12A 34B 56C 78D
# import threading
# import time
# def num():
# 	for i in range(1, 52, 2):
# 		lk2.acquire() # 获取全局解释器锁
# 		print(i, end='')
# 		print(i+1, end='')
# 		time.sleep(0.1) # 执行到此阻塞挂起
# 		lk1.release() #
#
# def pstr():
# 	for j in range(26):
# 		lk1.acquire()
# 		print(chr(j+ord('A')))
# 		time.sleep(0.1)
# 		lk2.release()
#
# lk1 = threading.Lock()
# lk2 = threading.Lock()
#
# t1 = threading.Thread(target=num)
# t2 = threading.Thread(target=pstr)
# lk1.acquire()  # 因为线程执行顺序是无序的，保证num()先执行
# t1.start()
# t2.start()

# 计算1990，1,1到2017,10,18的天数
# from datetime import datetime
# t = (datetime(2017,10,18)-datetime(1990,1,1)).days+1
# print(t % 5)


# import paramiko
#
# ssh = paramiko.SSHClient()
# ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy)
# ssh.connect(hostname='', username='', password='', port=22)
# stdin, stdout, stderr = ssh.exec_command('whoami')
# redata = stdout.read()
#
# ssh.close()

# a = [1, 2]
# print(id(a))
# a.append(3)
# print(a, id(a))

# s = 'ajldjlajfdljfddd'
# l = list(set(s))
# l.sort(reverse=False)
# print(''.join(l))

# def div1(x,y):
#     print("%s/%s = %s" % (x, y, x/y))
#
# def div2(x,y):
#     print("%s//%s = %s" % (x, y, x//y))
#
# div1(5,2)
# div1(5.,2)
# div2(5,2)
# div2(5.,2.)


# def multipliers():
#     return [lambda x: i * x for i in range(4)] # 真正调用i时 i的值已为3
#
# print([m(2) for m in multipliers()])

# # listt只进行一次初始化，没有指定该参数时，都是操作同一列表
# def lfun(var, listt=[]):
# 	# if listt is None:
# 	# 	listt = []
# 	listt.append(var)
# 	return listt
#
# a = lfun('a')
# b = lfun('b')
# c = lfun('c')
# print(a, b, c)


# import json
# i = 0
# with open('setting.txt') as f:
# 	for readlines in f:
# 		print(type(readlines), readlines)

# num = 8
# print(bin(num))
# print(~num)
# print(bin(~num))
# print(num << 1)


# def extend_list(val, list=[]):
# 	list.append(val)
# 	return list
#
# list1 = extend_list(10)
# list2 = extend_list(123, [])
# list3 = extend_list('a')
# print(list1)  # list1 = [10, 'a']
# print(list2)  # list2 = [123]
# print(list3)  # list3 = [10, 'a']


# def print_directry_contents(spath):
# 	import os
# 	files_list = os.listdir(spath)
# 	for file in files_list:
# 		pathfile = os.path.join(spath, file)
# 		if os.path.isdir(pathfile):
# 			print_directry_contents(pathfile)
# 		print(os.path.join(pathfile, file))
# print_directry_contents('E:\\day19\\day19\\')


# import os
# print(os.path.dirname(__file__))


# import threading
#
# def func(num):
# 	for j in range(num):
# 		print(j)
# 	print('thread-name {},id{}'.format(threading.current_thread().name, threading.current_thread().ident))
#
# t1 = threading.Thread(target=func, args=(5,), name='t1-thread')
# t2 = threading.Thread(target=func, args=(4,), name='t2-thread')
#
# # t1.start()
# # t2.start() # start()启动一个子线程，name为自定义的，id与其它子线程不同
#
# t1.run()
# t2.run() # run()不启动子线程，启动主线程，调用普通函数而已

# html = '''
# 	<head>
# 		<input class=text >标签内容</input>
# 	<head>
# 	'''
#
# import re
# res = re.findall(r'<.*?>', html)
# print(res)

# str1 = "北京市麦达技术数字有限公司"
# str2 = str1.replace("北京市","").replace("技术","").replace("有限","").replace("公司","")
# print(str2)
# import re
# str3 = re.sub(r'北京市|技术|有限|公司', repl='', string=str1)
# print(str3)

# str1 = 'HELLO PYTHON'
# with open('hello.txt','a') as f:
# 	for i in str1:
# 		f.write(i.lower())
# 		if i is ' ' :
# 			f.write('\n')

# import datetime
# def datanum(y, m, d):
# 	res = (datetime.datetime(y,m,d)-datetime.datetime(y, 1, 1)).days+1
# 	return res
# res = datanum(2018,12,27)
# print(res)


# str2 = '1.2.3.4.5'
# str3 = str2.split('.')
# str3.reverse()
# print('|'.join(str3))

# data_info = "现在的时间是：2018-3-10 11:52"
# import re
# pat = re.compile(r'\d{4}.\d{1,2}.\d{1,2}\s\d{1,2}:\d{1,2}')
# result = pat.findall(data_info)
# print(result)


# # 目录下3天前的文件，从中挑选出大小超过10M的删除掉。
# import os,datetime,time
# nowt = datetime.datetime.now()
# # print('当前时间日期：', nowt)
# oldt = datetime.timedelta(days=-3)
# rest = nowt+oldt
# # print('三天前的日期：', rest)
# ret = time.mktime(rest.timetuple())
# # print('三天前的时间戳：', ret)
# flist = os.listdir("D:\\")
# for i in flist:
# 	Bfile = os.path.join("D:\\", i)
# 	# print(Bfile)
# 	if os.path.getmtime(Bfile) > ret:
# 		Sizef = os.path.getsize(Bfile)
# 		if os.path.getsize(Bfile) > 1:
# 			print('三天内的文件：', Bfile, '大小：', Sizef)
# print(os.path.getsize("D:\\fa4f\\fastdfs (2).zip"))
# # print(os.stat("D:\\fa4f"))


# s = set([1,2,3,4])
# d = set([2,4,9,0,3])
# print(s|d)
# print(s&d)
# print(s^d)


# # 单例
# # __new__版
# class Ctest():
# 	_instance = None
# 	def __new__(cls, *args, **kwargs):
# 		if not cls._instance:
# 			cls._instance = super(Ctest, cls).__new__(cls, *args, **kwargs)
# 		return cls._instance
# # 装饰器版
# def gen(cls):
# 	print(cls.__name__)
# 	instance = {}
# 	def rest(cls, *args, **kwargs):
# 		if cls not in instance:
# 			instance[cls] = cls(*args, **kwargs)
# 		return instance[cls]
# 	return rest
# @gen
# class tst():
# 	pass
# a = tst()


# a = 1
# b = 2
# i, j = a+1, b+2
# print(i, j)

# #  reduce从py3以后被移除全局命名空间，添加到functools模块内
# import functools
# result = functools.reduce(lambda x,y:x*y,range(1,4))
# print(result)


# alist = [{"name":"a","age":20},{"name":"b","age":30},{"name":"c","age":25}]
# blist = sorted(alist, key=lambda x:x['age'], reverse=True)
# print(blist)

# 预产期计算
# import datetime
# import re
# sdate = input('请输入末次例假时间：')
# y, m, d = re.split(r' |,|\.', sdate)
# result = datetime.datetime(int(y)+1, int(m)-3, int(d)+7)
# print('您的预产期在 {} 附近！'.format(result.strftime('%Y-%m-%d')))


# class test(object):
# 	def __init__(self): # 前后__用于区分用户自定义的命名
# 		self._a = 'a' # 约定私有变量，不能被import导入
# 		self.__b = '123' #  防止和其他类相同的命名,
# 		self.str__ = 'c' # 防止和保留字符冲突
# class tet(object):
# 	def __init__(self):
# 		self.b = '123'
#
# obj = test()
# print(obj._a)
# # print(id(obj.b))
# print(id(obj._test__b)) # 双下划线开头的变量要这样使用：实例对象._类名__变量
# print(obj.str__)
# obj2 = tet()
# print(id(obj2.b))

# class A(object):
#        def __init__(self):
#               self.__private()
#               self.public()
#        def __private(self):
#               print('A.__private()')
#        def public(self):
#               print('A.public()')
# class B(A):
#        def __private(self):
#               print('B.__private()')
#        def public(self):
#               print('B.public()')
# b = B()
# #A.__private()
# #B.public()

# a = (1, 2, 3)
# print('{}'.format(a))
# print('%s' % a)

# from  multiprocessing import Pool, current_process
# import time, random
#
# def task1(*args, **kwargs):
# 	print('执行task1')
# 	print('参数：', args, kwargs)
# 	time.sleep(random.randint(1,3))
# 	print('结束task1')
#
# def task2():
# 	print('执行task2')
# 	time.sleep(random.randint(1,3))
# 	print('结束task2')
#
# if __name__ == '__main__':
# 	pool = Pool(2)
# 	pool.apply_async(task1, args=(1,2), kwds={'e':3, 'w':'1'})
# 	pool.apply_async(task2)
# 	print('任务提交完成')
# 	pool.close()
# 	pool.join()
# 	print('任务执行完毕')


# str1 = 'abcnd'
# list1 = [ord(x) for x in str1 if ord(x) < 127]
# print(list1)
# list2 = list(filter(lambda x :x < 127, map(ord, str1)))
# print(list2)

# i = 888
# def test_t():
# 	j = 999
#
# print(globals())


# arg1 = "{'k1':'v1', 'k2':'v2'}"
# print(type(arg1))
# print(type(eval(arg1)))


# def _recursion_merge_sort2(l1, l2, tmp):
#     if len(l1) == 0 or len(l2) == 0:
#         tmp.extend(l1)
#         tmp.extend(l2)
#         return tmp
#     else:
#         if l1[0] < l2[0]:
#             tmp.append(l1[0])
#             del l1[0]
#         else:
#             tmp.append(l2[0])
#             del l2[0]
#         return _recursion_merge_sort2(l1, l2, tmp)
#
# def recursion_merge_sort2(l1, l2):
#     return _recursion_merge_sort2(l1, l2, [])
#
# l1 = ['a', 'c', 'e']
# l2 = ['b', 'd', 'f']
# result = recursion_merge_sort2(l1, l2)
# print(result)


# l1 = ['a', 'b', 'c', 'd']
# l2 = ('a', 'b', 'c', 'd')
# l1.reverse()
# print(l1)
# for i in range(len(l2)-1,-1,-1):
# 	print(l2[i])

# tuple1 = ('bj', 'shunyi', 'xiaoqu')
# a, b, c = tuple1
# print(a,b,c,sep='!')

# alist = [{"name":"a","age":20},{"name":"b","age":30},{"name":"c","age":25}]
# alist.sort(key=lambda x:x['age'], reverse=True)
# print(alist)


# alist = ['a','b','c','d','e','f']
# blist = ['x','y','z','e','f']
# alist.extend(blist)
# clist = set(alist)
# print(clist)
# def func(*args):
# 	tmp = set()
# 	for i in args:
# 		tmp = tmp.union(i)
# 	print(tmp)
#
# func(alist, blist)

# tlist = ['a','b','c','d','e','f']
# import random
# random.shuffle(tlist)
# res = random.choice(tlist)
# print(res)
# print(tlist)

# # 栈结构，先进后出
# class Stack(object):
#     def __init__(self):
#         self.value = []
#
#     def push(self,x):
#         self.value.append(x)
#
#     def pop(self):
#         self.value.pop()
#
# stack = Stack()
# stack.push(1)
# stack.push(2)
# stack.push(3)
# print(stack.value)
# stack.pop()
# print(stack.value)

# import datetime
#
# def func(y, m, d):
# 	result = (datetime.datetime(y, m, d)-datetime.datetime(1989, 2, 26)).days+1
# 	return result
# d = func(2018, 11,28)
# print(d)


# l1 = 'k1:1|k2:2|k3:3'
# tmp = {}
# for i in l1.split('|'):
# 	k,v = i.split(':')
# 	tmp[k] = int(v)
# print(tmp)
# import re
# l2 = re.split(r':|\|', l1)
# l3 = {}
# for i in range(0,len(l2),2):
# 	l3[l2[i]] = int(l2[i+1])
# print(l3)

# arr = [[1,4,7,10,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
# def fun(num, arr):
# 	for x,i in enumerate(arr):
# 		for y,j in enumerate(i):
# 			if j == num:
# 				print('在数组的第{0}个元素内的第{1}个元素。'.format(x,y))
# 				return True
# 	return False
# status = fun(18, arr)
# print(status)


# a = 25
# b = 15
# def tun(a,b):
# 	while b:
# 		a, b = b, a%b
# 	return a
# r = tun(a,b)
# print(r)
# def fun(a,b):
# 	y = a*b
# 	while b:
# 		a, b = b, a%b
# 	return y//a
# r = fun(a,b)
# print(r)


# message = ('bj','sy','jx','xq')
# a,b,*c = message
# print(a,b,c)

# message = [('王野', '吉榆', '12345678'),
#            ('赵敏', '吉农', '88888888')]
# print('{:^15}|{:^9}|{:^9}'.format('名字', '籍贯','电话'))
# for n, j, p in message:
# 	print('{:15}|{:9}|{:9}'.format(n, j, p))

# import struct
# record = b'raymond   \x32\x12\x08\x01\x08'
# # name, serialnum, school, gradelevel = struct.unpack('<10sHHb', record)
# # print(name, serialnum, school, gradelevel)
# from collections import namedtuple
# Student = namedtuple('tn', 'name serialnum school gradelevel')
# # print(Student._make(struct.unpack('<10sHHb', record)))
# # print(Student.name, Student.serialnum, Student.school, Student.gradelevel)
# # tk = Student('wangye', 9527, 'siping', 'zd')
# # print(tk)
# tk = ['wangye', 9527, 'siping', 'zd']
# tkt = Student._make(tk)
# print(tkt)


# invoice = """
# 0.....6................................40........52...55........
# 1909   Pimoroni PiBrella                  $17.50   3    $52.50
# 1489   6mm Tactile Switch x20             $4.95    2    $9.90
# 1510   Panavise Jr. - PV-201              $28.00   1    $28.00
# 1601   PiTFT Mini Kit 320x240             $34.95   1    $34.95
# """
# SKU = slice(0, 6)
# DESCRIPTION = slice(6, 40)
# UNIT_PRICE = slice(40, 52)
# QUANTITY = slice(52, 55)
# ITEM_TOTAL = slice(55, None)
# line_items = invoice.split('\n')[2:]
# for item in line_items:
# 	print(item[DESCRIPTION],':',item[ITEM_TOTAL])

# import dis
# dis.dis('s[a] += b')

# l1 = ['wdff', 'tr', 'vdcd', 'popi']
# l1.sort(key=lambda x:x.lower())
# print(l1)


# import bisect
# import sys
# HAYSTACK = [1, 4, 5, 6, 8, 12, 15, 20, 21, 23, 23, 26, 29, 30]
# NEEDLES = [0, 1, 2, 5, 8, 10, 22, 23, 29, 30, 31]
# ROW_FMT = '{0:2d} @ {1:4d} {2}{0:<2d}'
# def demo(bisect_fn):
# 	for needle in reversed(NEEDLES):
# 		position = bisect_fn(HAYSTACK, needle)
# 		offset = position * '  |'
# 		print('{0:2d} @ {1:4d} {2}{0:<2d}'.format(needle, position, offset))
# if __name__ == '__main__':
# 	if  sys.argv[-1] == 'left':
# 		bisect_fn = bisect.bisect_left
# 	else:
# 		bisect_fn = bisect.bisect
# 	print('DEMO:', bisect_fn.__name__)
# 	print('haystack ->', ' '.join('%2d' % n for n in HAYSTACK))
# 	demo(bisect_fn)

# import bisect
# st1 = [1, 4, 5, 6, 8, 12, 15, 20, 21, 23, 23, 26, 29, 30]
# res = bisect.bisect(st1, 16) #返回值为16在st1序列小值值最近的位置
# print(res)


# import random
# import bisect
# mlist = []
# for i in range(1,10):
# 	t = random.randrange(20)
# 	bisect.insort(mlist, t) # 插入按照排序数据，全部插入完毕无需在进行排序
# 	print('{:2}->{}'.format(t,mlist))
# # print(random.randrange(8))

# import array
# import random
# fls = array.array('d', (random.random() for i in range(10**7)))
# print(fls[-1])
# fp = open('array1.bin', 'wb')
# fls.tofile(fp)
# fp.close()
# fls2 = array.array('d')
# fp = open('array1.bin', 'rb')
# fls2.fromfile(fp, 10**7)
# print(fls2[-1])
# fp.close()

# import random
# with open('ft.txt', 'w') as f:
# 	for i in range(1000, 9999):
# 		f.write('{}\n'.format(random.random()*10000))
# import time, linecache
# with open('ft.txt', 'r') as f:
# 	for line in f: # 自动的使用buffered IO以及内存管理
# 		print(line)
# # 	while True:
# # 		data = f.read(5)
# # 		print(data)
# # 		time.sleep(0.5)
# # 		if not data:
# # 			break

# import array
# numbers = array.array('h', [-2, -1, 0, 1, 2])
# memv = memoryview(numbers)
# print(len(memv))
# print(memv[0])
# memv_oct = memv.cast('B')
# print(memv_oct.tolist())
# memv_oct[5] = 4
# print(numbers)

# from collections import namedtuple
# St = namedtuple('cc', 'name age thone')
# obj = St('wangye', 30, 123123123)
# print(obj)

# import numpy
# # a = numpy.arange(24)
# # print(a)
# # print(a.shape)
# # a.shape = 3,8 # 生成三行四列的二维数组，形状
# # # a.shape = 2,3,4 #
# # # print(a)
# # # print(a[1, 2, 2]) # 第一组第二行第二个数据
# # print(a)
# # print('打印第一列：',a[:,1])
# # print('打印第二行', a[2])
# # print(a.transpose()) # 行变列，列变行，原数据不变，颠倒
# fls = numpy.loadtxt('ft.txt') # 读取文件
# print(fls[-3:]) # 输出后三个元素
# fls *= 0.5 # 元素均乘以0.5
# print(fls[-3:])
# numpy.save('ft.npy', fls) # 保存成ft.npy文件
# fls2 = numpy.load('ft.npy', 'r+') # 载入文件
# print(fls2[-3:])


# from collections import deque # 双向队列
# dq = deque(range(10), maxlen=10) # maxlen一旦设定，不能修改
# print(dq)
# dq.rotate(3) # 旋转，N大于0时,队列右侧的N个元素移动到左侧，小于0时相反
# print(dq)
# dq.rotate(-3)
# print(dq)
# dq.appendleft(66) # 左侧添加元素，右侧末端的元素被删除
# print(dq)
# dq.append(88) # 右侧侧添加元素，左侧末端的元素被删除
# print(dq)
# dq.extendleft([33,44,55]) # 左侧添加N个元素，右侧末端依次N个元素被删除
# print(dq)
# dq.extend([33,44,55]) # 右侧添加N个元素，左侧末端依次N个元素被删除
# print(dq)
# dq.pop() # append 和popleft都是原子操作，可以在多线程中安全当做先进先出的栈使用，不用担心资源锁
# print(dq)
# dq.popleft()
# print(dq)
# dq.clear()
# print(dq)

# a = [i** 2 for i in range(10) if i > 4]
# print(a)
# b = (i** 2 for i in range(10) if i > 4)
# print(b)
# for i in b:
# 	print(i)

# DIAL_CODES = [	(86, 'China'),
# 				(91, 'India'),
# 				(1, 'United States'),
# 				(62, 'Indonesia'),
# 				(55, 'Brazil'),
# 				(92, 'Pakistan'),
# 				(880, 'Bangladesh'),
# 				(234, 'Nigeria'),
# 				(7, 'Russia'),
# 				(81, 'Japan')]
#
# dict_code = {name.upper():code for code, name in DIAL_CODES} # 字典推导式
# print(dict_code)
# filter_ = {n:c for n,c in dict_code.items() if c > 50 }
# print(filter_)


# print(chr(65))
# print(chr(90))
# print(chr(97))
# print(chr(122))
# import random
# import string
# ran_str = ''.join(random.sample((string.ascii_letters + string.digits), 8))
# print(ran_str)
# # print(type(string.ascii_letters + string.digits))


# a = [[]] *10
# for i in range(10):
# 	print(id(a[i]))
#
# b = []
# print('---')
# for i in range(10):
# 	b.append([])
# for i in range(10):
# 	print(id(b[i]))

# import requests
# from urllib import request
# data = request.urlopen('https://kyfw.12306.cn/otn/resources/login.html')
# print(data.read().decode('utf-8'))

# from splinter.browser import Browser
# import time
# bwr = Browser(driver_name='chrome') # 选定浏览器驱动
# bwr.visit('https://github.com/login') # 打开url
# time.sleep(5)
# bwr.fill('login', 'smartwy') # 当前页面的name=login的标签添加数据
# time.sleep(0.5)
# bwr.fill('password', 'Wangye13141314')# 当前页面的name=password的标签添加数据
# # bwr.find_by_text('Sign in').click()
# bwr.find_by_value('Sign in').click() # 点击value=Sign in的按钮
# time.sleep(1)
# # bwr.fill('name', 'mt-1').click()
# # time.sleep(1)
# # bwr.find_by_text('Your repositories').click()
# bwr.visit('https://github.com/smartwy?tab=repositories')

# from functools import partial
# # 偏函数
# def mod(n, m):
# 	return n % m
#
# mod_by_100 = partial(mod, 100)
#
# print(mod(100, 7))
# print(mod_by_100(7))
# int5 = partial(int, base=2)
# print(int5('100001'))

# j = 0
# for i in dir(__builtins__):
# 	j += 1
# print('内置函数有{}个'.format(j))


# class tff():
# 	_instance = []
# 	def __new__(cls,*args,**kwargs):
# 		if not cls._instance:
# 			cls._instance = super(tff, cls).__new__(cls, *args,**kwargs)
# 		return cls._instance

# # 斐波那契
# i = 0
# j = 1
# for x in range(10):
# 	i,j = j+i,i
# 	print(i)

# def fib(max):
#     n,a,b = 0,0,1
#
#     while n < max:
#         #print(b)
#         yield  b #只要是含有yield关键字就是生成器 可以yield多次 yield保存函数的状态
#         a,b = b,a+b
#
#         n += 1
#
# t = fib(10)
#
# print(t.__next__()) #生成器自动实现了迭成器,所以会有__next__()方法。
# print(t.__next__()) #运行一次，相当于保存的是上一次内存里状态的结果

# 反序
# list1 = [1, 3, 6, 9]
# list1.reverse()
# print(list1)
#
# for i in range(len(list1)-1, -1, -1):
# 	print(list1[i])


# tempstr = "hello you hello python are you ok"
# res = tempstr.replace('hello', '666')
# print(res)
# state = tempstr.find('ok')
# print(state)
#
# import re
# res = re.sub('hello','666', tempstr)
# print(res)
# res = re.search('hello', tempstr)
# print(res)

# class  one(object):
# 	_instance = None
# 	def __new__(cls,*args, **kwargs):
# 		if not cls._instance:
# 			cls._instance = super(one, cls).__new__(cls, *args, **kwargs)
# 		return cls._instance
#
#


# st1 = '  sdf df d sf '
# print('切割两端空格：' ,st1.strip())
# print('切割首端空格：' ,st1.lstrip())
# print('切割末端空格：',st1.rstrip())
# print(st1)
# print('指定切割：', st1.split('d'))


# alist = [{'name':'wddd','age':18},{'name':'zii', 'age':13}, {'name':'add','age':19}]
# blist = sorted(alist,key=lambda x:(x['name'], x['age']), reverse=True)
# print(blist)
# alist.sort(key=lambda x:(x['name'], x['age']), reverse=True)
# print(alist)

# a = ['a', 'b', 'c']
# b = ['b', 'i', 't']
# a.extend(b)
# print(set(a))
# s = set()
# s = s.union(a)
# s = s.union(b)
# print(s)
# print(a.count('a'))

# from random import shuffle, sample
# a = ['a', 'b', 'c']
# shuffle(a) # 打乱顺序
# print(a)
# print(sample(a, 2)) # 随机弹出元素

# from datetime import datetime
# def dt(y, m, d):
# 	return (datetime(y, m, d)-datetime(y, 1,1)).days+1
# res = dt(2018,4,4)
# print(res)

# import re
# d1 = {}
# al = "k1:1|k2:2?k3:3"
# # data = al.split('|')
# data = re.split('\||\?', al)
# for kv in data:
# 	k, v = kv.split(':')
# 	d1[k] = int(v)
# print(d1)

# arr = [[1,4,7,10,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
# data = int(input("Please input number :"))
# for i in arr:
# 	if data in i:
# 		print('ok')
# 	else:
# 		print('no')

# 最小公倍数
# a= 25
# b=15
# while b:
# 	a, b = b, a%b
# print(a)
# a= 25
# b=15
# 最大公约数
# c = a*b
# while b:
# 	a, b = b, a%b
# print(c//a)

# 中位数，长度是偶数的取中间两数的平均数
# def mnum(num):
# 	llnum = len(num)
# 	if llnum%2 == 1:
# 		fres = llnum//2+1
# 		print(fres)
# 	else:
# 		fres = len(num)//2-1
# 		num.sort()
# 		print((num[fres]+num[fres+1])/2)
#
# res = mnum([1,3,5,4,6,7,8,2])


# #处理数组矩阵
# arr = [[1,4,7,10,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
# def get_num(num,data=None):
#     while data:
#         if num > data[0][-1]:
#             del data[0]
#         elif num<data[0][-1]:
#             for i in data[0]:
#
#         else:
#             return True
#             # data.clear()
#     return True
# print(get_num(10,arr))


# import webbrowser
#
# webbrowser.open('www.baidu.com',new=2)

# ls = ['217.169.209.2:6666', '192.227.139.106:7808', '110.4.12.170:83', '69.197.132.80:7808', '205.164.41.101:3128', '63.141.249.37:8089', '27.34.142.47:9090']
# t = tuple(ls)
# print(t)

# import re
# str1 = 'abd ddd re'
# res = re.sub('re', 'qq',str1)
# print(res)

# import shutil
#
# shutil.copyfile('F:\应用整理.txt', 'E:\day19\应理.txt') # 目标目录要写拷贝后文件名称

# b1=[1,2,3]
# b2=[2,3,4]
# b3 = [i for i in b1 if i in b2]
# print(b3)
# b1.extend(b2)
# b4 = [i for i in b1 if i not in b3]
# print(b4)

# import json
# p = json.loads('{"persons":[{"name":"yu","age":"23"},{"name":"zhang","age":"34"}]}')
# print(p)
# print(p['persons'][0]['name'])

# numbers = [1,3,5,7,8,2,4,20]
#
# total=sum(numbers)
# fore=0
# for number in numbers:
#    if fore == (total - number) / 2:
#       print(number)
#    else:
#       fore += number

# a = 'dwfokdva'
# t = ''
# print(a[::-1])
# for i in range(len(a)-1,-1,-1):
# 	t += a[i]
# print(t)

# import os
# count = 0
# os.chdir(r'C:\Users\Administrator\Desktop')
# with open('initscript.txt','r') as init:
# 	for i in init.read():
# 		if i.isupper():
# 			count += 1
# 	print(count)

# # @classmethod
# class BasT(object):
# 	__num = 0
# 	@classmethod
# 	def addnum(cls):
# 		cls.__num += 1
# 	@classmethod
# 	def getnum(cls):
# 		return cls.__num
# 	def __new__(cls, *args, **kwargs):
# 		BasT.addnum()
# a = BasT()
# b = BasT()
# print(BasT.getnum())

# import time
#
# class TimeTest(object):
#     def __init__(self, hour, minute, second):
#         self.hour = hour
#         self.minute = minute
#         self.second = second
#
#     @staticmethod
#     def showTime():
#         return time.strftime("%H:%M:%S", time.localtime())
#
# print(TimeTest.showTime())
# t = TimeTest(2, 10, 10)
# nowTime = t.showTime()
# print(nowTime)


# lt = ['a','b','c','d']
#
# dt = {k:v for k,v in enumerate(lt,1)}
# print(dt)


# class A():
#     def foo1(self):
#         print("A")
# class B(A):
#     def foo2(self):
#         pass
# class C(A):
#     def foo1(self):
#         print("C")
# class D(B, C):
#     pass
#
# d = D()
# d.foo1()

# import copy
# a = [1, 2, 3, 4, ['a', 'b']]  #原始对象
#
# b = a  #赋值，传对象的引用
# c = copy.copy(a)  #对象拷贝，浅拷贝
# d = copy.deepcopy(a)  #对象拷贝，深拷贝
#
# a.append(5)  #修改对象a
# a[4].append('c')  #修改对象a中的['a', 'b']数组对象
#
# print('a = ', a)
# print('b = ', b)
# print('c = ', c)
# print('d = ', d)


# arg1 = [['a','c'] * 3] *3
# print(arg1)
# arg1[1][2] = 'wwww'
# print(arg1)
# arg2 = [['a','c'] * 3  for i in range(3)]
# print(arg2)
# arg2[1][2] = 'tttt'
# print(arg2)


# class objt():
# 	_instance = None
# 	def __new__(cls, *args, **kwargs):
# 		if not cls._instance:
# 			cls._instance = super(objt, cls).__new__(cls)
# 		return cls._instance
# a = objt()
# print(id(a))
# b = objt()
# print(id(b))

# result = sum([i for i in range(1,10**8+1)])
# print(result)


# def huiwen(arg1):
# 	if len(arg1) < 2:
# 		return True
# 	if arg1[0] == arg1[-1]:
# 		return huiwen(arg1[1][-1])
# 	else:
# 		return False
# s1 = input('input :')
# if huiwen(s1):
# 	print('ok')
# else:
# 	print('no')


# for i in range(1,10):
# 	for j in range(1,i+1):
# 		print('{} * {} = {}  '.format(i,j,i*j),end='')
# 		if i == j:
# 			print('\n')
#

# import string
# l1 = [ i for i in string.ascii_lowercase]
# d1 = { k:v for k,v in enumerate(l1,1)}
# print(d1)


# import sys
# a = 'abc'
# b = 'abc'
# print(sys.getrefcount(b))



# def tfun():
# 	temp = [lambda x:x*i for i in range(4)]
# 	print(temp)
# 	return temp
# for a in tfun():
# 	print(a(2))


# l1 = ['a','g','e']
# print(l1[4:]) # 输出[]，而不是indexerror


# li=(i**2 for i in range(5))
# print(li)
# for x in range(5):
# 	print(next(li))


# list = ['a','a','a',1,2,3,4,5,'A','B','C']
# a,b,c,*arg,e,f,g = list
# print(arg)


# portfolio = [
#     {'name': 'IBM', 'shares': 100, 'price': 91.1},
#     {'name': 'AAPL', 'shares': 50, 'price': 543.22},
#     {'name': 'FB', 'shares': 200, 'price': 21.09},
#     {'name': 'HPQ', 'shares': 35, 'price': 31.75},
#     {'name': 'YHOO', 'shares': 45, 'price': 16.35},
#     {'name': 'ACME', 'shares': 75, 'price': 115.65}
# ]
#
# result = sorted(portfolio,key=lambda i :i['price'],reverse=True)
# print(result)
# res = max(portfolio,key=lambda i :i['price'])
# print('max:',res)
# res = min(portfolio,key=lambda i :i['price'])
# print('min:',res)

# import time
# def fib(n):
#     a, b = 0, 1
#     for _ in range(n):
#         a, b = b, a + b
#         yield a
#
# def main():
#     for val in fib(10):
#         time.sleep(1)
#         print(val)
# if __name__ == '__main__':
#     main()


# import os
# import time
#
# def main():
#     content = 'abcdefghijklmnopqrstuvwxyz'
#     while True:
#         # 清理屏幕上的输出
#         os.system('cls')
#         # os.system('clear')
#         print(content)
#         # 休眠200毫秒
#         time.sleep(0.2)
#         content = content[1:] + content[0]
#
# if __name__ == '__main__':
#     main()

# import psutil
# mem = psutil.virtual_memory()
# memtotal = mem.total/1024/1024
# memused = mem.used/1024/1024
# baifen = memused/memtotal*100
# print('总内存：%.1f MB' % memtotal)
# print('已使用：%.1f MB' % memused)
# print('使用率：{0:.2f}%'.format(baifen))
# cpuu = psutil.disk_usage('E://')
# cpuu = cpuu.used/1024/1024/1024
# print(cpuu)
# nett = psutil.net_if_addrs()
# print(nett['本地连接 2'])


# # 变量作用域遵循LEGB，当前函数作用域，外部函数作用域，全局作用域，内置作用域
# def f1():
# 	i = 'f1'
# 	def f2():
# 		j = 'f2'
# 		def f3():
# 			x = 'f3'
# 			print(locals())
# 		f3()
# 	f2()
# f1()

# # 先取列表中索引是偶数的数字，然后过滤掉所有的奇数.
# list = [ 1 , 3 , 5 , 8 , 10 , 13 , 18 , 36 , 78 ]
# result = [ i for i in list[::2] if i%2 == 0]
# print(result)

# class dan(object):
# 	_instance = None
# 	def __new__(cls, *args, **kwargs):
# 		if cls._instance in None:
# 			cls._instance = object.__new__(cls,*args,**kwargs)
# 		return cls._instance


# import psutil
# r = psutil.net_io_counters()
# print(r.bytes_recv)

# import time
# import matplotlib.pyplot as plt
# import numpy as np
# import math
# def Method_Improve(point):
#     def initial(ax):
#         ax.axis("equal") #设置图像显示的时候XY轴比例
#         ax.set_xlabel('Horizontal Position')
#         ax.set_ylabel('Vertical Position')
#         ax.set_title('Vessel trajectory')
#         plt.grid(True) #添加网格
#         return ax
#
#     es_time = np.zeros([point])
#     fig=plt.figure()
#     ax=fig.add_subplot(1,1,1)
#     ax = initial(ax)
#     plt.ion()  #interactive mode on
#     IniObsX=0000
#     IniObsY=4000
#     IniObsAngle=135
#     IniObsSpeed=10*math.sqrt(2)   #米/秒
#     print('开始仿真')
#     obsX = [0,]
#     obsY = [4000,]
#     for t in range(point):
#         t0 = time.time()
#         #障碍物船只轨迹
#         obsX.append(IniObsX+IniObsSpeed*math.sin(IniObsAngle/180*math.pi)*t)
#         obsY.append(IniObsY+IniObsSpeed*math.cos(IniObsAngle/180*math.pi)*t)
#         plt.cla()
#         ax = initial(ax)
#         ax.plot(obsX,obsY,'-g',marker='*')  #散点图
#         #下面的图,两船的距离
#         plt.pause(0.001)
#         es_time[t] = 1000*(time.time() - t0)
#     return es_time
# Method_Improve(1)


# import os
# path = os.path.realpath(__file__)
# print(path)
# rpath = os.path.dirname(path)
# print(rpath)

# import psutil
# print(psutil.net_io_counters().bytes_recv,psutil.net_io_counters().bytes_sent,psutil.net_if_addrs())

# import matplotlib
# data = str(help(matplotlib))
# print(data)
# with open('matplotlib_helpinfo.txt', 'w',encoding='utf-8') as f:
# 	f.write(data)

# import numpy as np
# linspace(start, stop, num=50, endpoint=True, retstep=False, dtype=None)
# 在规定的时间内，返回固定间隔的数据。
# 他将返回“num”个等间距的样本，在区间[`start`, `stop`]中。其中，区间的结束端点可以被排除在外。
# print(np.linspace(-10, 10, 500)) # 500个数，-10~10等间隔数据

# dlist = np.arange(0, 400, 10) # 0start  400stop 10step
# print(dlist)
# d = np.random.rand(1,)
# print(d)
# tl = np.logspace(1, 10,10)
# print(tl)
# data = np.ones((5,5))
# print(data)
# data = np.zeros((5,5))
# print(data)
# data = np.eye(2,4)
# print(data)
# # np.set_printoptions(threshold='nan')
# data = np.empty((4,5))
# print(data)
#
# a = 'abcd'
# print(np.fromstring(a,dtype=np.int8))
# a = np.random.random((2,4))
# print(a)
# a = [1,2,3,4,5]
# np.random.shuffle(a)
# print(a)

# def create_counter(n):
# 	print("create_counter")
# 	while True:
# 		print('ttt')
# 		yield n
# 		print("increment n")
# 		n += 1
#
#
# gen = create_counter(2)
# print(gen)
# print(next(gen))
# print(next(gen))

# import tensorflow as tf
#
# v1 = tf.constant([[2,3]])
# # print(v1)

# import random
# l1 = ['a','b','c','d']
# random.shuffle(l1)
# print(l1)
# print(random.sample(l1,1))


# 有10个人要互赠礼物，要求：
# 1.每个人都要收到一份礼物
# 2.每个人都要送出一份礼物
# 3.不能送给自己
# import random
# import itertools
#
# g_list=[]
#
# for i in range(1,11,1):
#     g_list.append(i)
#
# print(g_list)
#
# map_people = []
#
# #生成二维数组，每一行代表一个学生，第一个数据为学生编码，第二个为拥有的礼物，第三个为收到的礼物
#
# for i in range(0, 10):
#     map_people += [[]]
#     map_people[i] += [i+1]
#     map_people[i] += [1]
#
# print("原始数据")
# print(map_people)
#
# for i in range(10):
#     j = random.randint(0, 9)
#     while(i == j):
#         # j = random.randint(0, 9)
#         map_people[i][1] = map_people[i][1] - 1
#         map_people[j][2] = map_people[j][2] + 1
#         print("%d  =>  %d" % (i,j))
#
# print("第一轮：随机赠送，每人都要赠出礼物，得到的列表")
# print(map_people)
#
# for k in range(10):
#     if map_people[k][2] > 1:
#         for m in range(10):
#             if map_people[m][2] == 0:
#                 if map_people[k][2] > 1 :
#                     map_people[k][2] = map_people[k][2] - 1
#                     map_people[m][2] = map_people[m][2] + 1
#                     print("%d  =>  %d" % (k,m))
#
# print("第二轮：得到礼物大于1的，把多的礼物赠与无礼物的人，得到的列表")
#
# print(map_people)


# import requests
# import json
#
# data = requests.post('https://www.baidu.com', data=json.dumps({'some': 'data'}), headers={'content-type': 'application/json'})
# # print(data.text)
# print(data.cookies)

# import re
# print(dir(re))
# data = 253
# s1 = str(bin(data))
# print(s1)
# print(re.sub('0b', string=s1, repl='0000'))
# # print(dir(bin))

# res = (i for i in range(10))
# print(sum(res))

# st1 = 'config.cfg'
# status = st1.endswith('.cfg')
# print(status)

# tt = dict.fromkeys(['k1','k2'],[])
# print(tt)
# tt['k1'].append(666)
# print(tt)
# tt['k1'] = 777
# print(tt)

# print('\n'.join([' '.join(['%s * %s = %s'%(y, x, x*y) for y in range(1, x+1)]) for x in range(1, 10)]))

# print('\n'.join([' '.join(['%s * %s = %s' % (y, x, x*y) for y in range(1,x+1)]) for x in range(1,10)]))

# userinfo = {
# 	'1':{
# 			'name':'wy',
# 			'id':1234567889,
# 			'sex':'man',
# 			'age':30,
# 			'addr':'北京顺义',
# 			'tel':188888888888,
# 		}
# }
# print(userinfo['1']['name'],type(len(userinfo.keys())))

# import time
# # print(help(time.strftime))
# print(time.strftime('%Y-%m-%d %H:%M:%S'))

# a = 'asdfasdf'
# print(a[::-1])

# 无重复字符的最长子串，
# def lengthOfLongestSubstring(s: str) -> int: # 指定参数及返回值类型
# 	# 获取字符串s对应的列表
# 	s_to_list = list(s)
# 	stack = []
# 	max_length = 0
# 	for index in s_to_list:
# 		if index not in stack:   # 如果stack栈中不包含index元素，则可以进栈
# 			stack.append(index)
# 			max_length = max(max_length, len(stack))
# 		else:   # 如果stack栈中包含index元素，则要将前面index元素之前的数都得拿出栈
# 			start = stack.index(index) # 得出重复字符的索引
# 			stack = stack[start + 1:] # 选出重复字符的索引后一个元素至最后
# 			stack.append(index)   # 添加元素
# 	print(stack)
# 	return max_length
# l = 'abcabcdweiropoiuytrewq'
# result = lengthOfLongestSubstring(l)
# print(result)

# def lengthOfLongestSubstring(s: str) -> int: # 指定参数及返回值类型
# 	s_list = list(s)
# 	stack = []
# 	m_l = 0
# 	for arg in s_list:
# 		if arg not in stack:
# 			stack.append(arg)
# 			m_l = max(m_l, len(stack))
# 		else:
# 			start = stack.index(arg)
# 			stack = stack[start + 1:]
# 			stack.append(arg)
# 	data = ''.join(stack)
# 	print(data)
# 	return m_l
# l = 'abcabcdweiropoiuytrewqo'
# result = lengthOfLongestSubstring(l)
# print(result)


# import json # 序列化练习
#
# # load 反序列化 将json格式文件内容转字典
# result = json.load(open('ft.txt', 'r'))
# print(result)
#
# # loads 反序列化 内存对象，例 字符串转字典
# res = json.loads('{"a":1,"b":2,"c":3,"d":4,"e":5}')
# print(res)
#
# # dump 字典转json格式，存储
# dict_1 = {'code':'200', 'message':'ok'}
# json.dump(dict_1, open('ft.txt', 'w'))
#
# # dumps 字典转json string，易传输
# str_1 = {"code":"200", "message":"ok"}
# resu = json.dumps(str_1)
# print(resu)


# s = 'asdfasf.v.d.e.d.d'
# res = s.split('.')
# print(res)
#
# s = '   qwef sdfvae   '
# print(s.lstrip(),'\n',s.strip(),'\n',s.rstrip())

# # a+b+c=1000 且a*2+b*2=c*2
# import time
# s = time.time()
# for a in range(0,1001):
# 	for b in range(0,1001-a):
# 		for c in range(0,1001-a-b):
# 			if a+b+c == 1000 and a*a + b*b == c*c:
# 				print(a,b,c)
# print(time.time()-s)

# lst = [9,8,7,20]
# first, *second = lst
# head, *_, tail = lst
# print(head)
# print(tail)

# a,c,b = "JAVA_HOME=/usr/bin".partition('=')
# print(a,'--',b)


# print([(i,j) for i in range(7) if i>4 for j in range(20,25) if j>23])
# print([(i,j) for i in range(7) for j in range(20,25) if i>4 if j>23])
# print([(i,j) for i in range(7) for j in range(20,25) if i>4 and j>23])


# class Point():
# 	def __init__(self, x ,y):
# 		self.x = x
# 		self.y = y
# 	def __call__(self, *args, **kwargs):
# 		return "Point {}:{}".format(self.x, self.y)
#
# p = Point(4,5)
# print(p)
# print(p())

# class Adder:
# 	def __call__(self, *args, **kwargs):
# 		ret = 0
# 		for x in args:
# 			ret += x
# 		self.ret = ret
# 		return ret
# adder = Adder()
# print(adder(4,5,6))
# print(adder.ret)


# s1 = '3.90mog/s'
# print(s1.strip('mog/s')) # 默认删除空格
# print(s1.split('mog/s')) # 指定切割符

# import os
# def dir_pf(d_path):
# 	for s_child in os.listdir(d_path):
# 		s_child_path = os.path.join(d_path, s_child)
# 		if os.path.isdir(s_child_path):
# 			dir_pf(s_child_path)
# 		else:
# 			print(s_child_path)
# dir_pf('D:\Bypass')

# print('asdf'[::-1])

# kd = {}
# s1 = 'k:1 |k1:2|k2:3|k3:4'
# for i in s1.split('|'):
# 	k,v = i.split(':')
# 	kd[k] = v
#
# print(kd)

# alist = [{'name':'a','age':20},{'name':'b','age':30},{'name':'c','age':25}]
# print(sorted(alist, key=lambda i:i['age']))

# list = ['a','b','c','d','e']
# print(list[10:]) # 索引切片不会报indexerror，直接用超出索引会报indexerror


# print([i*4 for i in range(10)]) # 等差是4的列表

# list1 = [1,2,3]
# list2 = [3,4,5]
# s1 = set(list1)
# s2 = set(list2)
# print(s1 & s2) # 交集
# print(s1 ^ s2) # 差集

# l1 = ['b','c','d','c','a','a']
# # print(set(l1))
# l2 = sorted(set(l1),key=l1.index)
# print(l2)

## 反转一个整数
# def fanzhuan(num):
# 	if -10 < num < 10:
# 		return num
# 	if num < 0:
# 		num = str(num)
# 		s = num[:0:-1]
# 		return '-' + s
# 	else:
# 		num = str(num)
# 		return num[::-1]
#
# print(fanzhuan(123))


# print(sum(range(1,101)))
#
# a=[1,2,3,4,5,6,7,8]
# print(id(a))
# for i in range(len(a)-1,-1,-1):
#     if a[i]>5:
#         pass
#     else:
#         a.remove(a[i])
# print(id(a))
# print('-----------')
# print(a)
#
# a=[1,2,3,4,5,6,7,8]
# b = filter(lambda x: x>5,a)
# print(list(b))

# a = [1,2,3,4]
# for i in range(len(a)-1,-1,-1): # 索引倒序
# 	print(i)


# # 给定nums = [2,7,11,15],target=9 因为 nums[0]+nums[1] = 2+7 =9,所以返回[0,1]
# ns = [2,7,11,15]
# sl = 9
# def zw(nums,s):
# 	for i_idx,i in enumerate(nums):
# 		for j_idx,j in enumerate(nums):
# 			if i+j == s:
# 				return i_idx,j_idx
# print(zw(ns,sl))


import re


# # 方法一
# def test(filepath):
# 	distone = {}
# 	with open(filepath) as f:
# 		for line in f:
# 			line = re.sub("\W+", " ", line)
# 			lineone = line.split()
# 			for keyone in lineone:
# 				if not distone.get(keyone):
# 					distone[keyone] = 1
# 				else:
# 					distone[keyone] += 1
# 	num_ten = sorted(distone.items(), key=lambda x: x[1], reverse=True)[:10]
# 	num_ten = [x[0] for x in num_ten]
# 	return num_ten
# result = test(r'E:\python_project_dir\python_test\test.txt')
# print(result)


import datetime

# # y = int(input('年>>>'))
# # m = int(input('月>>>'))
# # d = int(input('日>>>'))
# y,m,d = input('>>>').split()
# y, m, d = int(y),int(m), int(d)
# ndate = datetime.date(y,m,d)
# odate = datetime.date(y,1,1)
# result = ndate - odate
# print(result)

# 思路：先降序排列，遍历每个元素，奇数insert 0 最后形成前面奇数小到大后面偶数大到小
# def func1(l):
#     if isinstance(l, str):
#         l = [int(i) for i in l]
#     l.sort(reverse=True)
#     print(l)
#     for i in range(len(l)):
#         if l[i] % 2 > 0:
#             l.insert(0, l.pop(i))
#     print(''.join(str(e) for e in l))
# l = '1982376455'
# func1(l)

# l2 = [1,2,3,4,5,6,7]
# res = l2.pop(2) # 指定索引
# res1 = l2.remove(2) # 指定元素内容
# print(res,l2)

# num_list = [34, 11, 23, 56, 78, 0, 9, 12, 3, 7, 5]
# # num_list.sort() # 原地排序
# # print(num_list,num_list[-2])
# res = sorted(num_list) # 排序新生成列表
# print(num_list, res[-2])


# s1 = "AAABBCCAC"
# st1 = set(s1)
# for i in st1:
# 	res = s1.count(i)
# 	print(i,':',res)


# from collections import Counter
# print(Counter("AAABBCCAC").most_common())
# print("".join(map(lambda x: x[0] + str(x[1]), Counter("AAABBCCAC").most_common())))



# def f(i:int,name:str) -> int:
# 	s = name + str(i)
# 	return s
# res = f(4,'wy')
# print(res)


# def multipliers():
#     return [lambda x: i *x for i in range(4)]
# print([m(2) for m in multipliers()])


# class Abc(object):
# 	__instance = None
# 	def __new__(cls, *args, **kwargs):
# 		if cls.__instance is None:
# 			cls.__instance = super(Abc,cls).__new__(cls)
# 		return cls.__instance

# import time
#
# def timeit(func):
# 	def wrapper(*args, **kwargs):
# 		start = time.clock()
# 		ret = func(*args, **kwargs)
# 		end = time.clock()
# 		print('used:', end - start)
# 		return ret
#
# 	return wrapper
#
# @timeit
# def foo():
# 	print('in foo()')
# foo()

# import time
# print(time.clock(),time.time(),sep='|')

# print ([[x for x in range(1,100)][i:i+3] for i in range(0,100,3)])


# import random
# tuple1 = ['23','4', 'adf']
# print(random.random()) # 0-1
# print(random.randint(0,11)) # 0-10
# print(random.randrange(0,10,3)) # 0 3 6 9
# print(random.sample(tuple1, k=2)) # 随机输出k个元素
# print(random.shuffle(tuple1),tuple1) # 可变类型数据，原址打乱顺序

