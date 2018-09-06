# -*- coding:utf-8 -*-
#Name:     
#Descripton: sqlAlchemy是python中最著名的ORM(Object Relationship Mapping)框架,可以把model中的模型和数据库中的一条数据相互转换的工具。
#            最初主要描述的是程序中的Object对象和关系型数据库中Rlation关系(表)之间的映射关系，
#            目前来说也是描述程序中对象和数据库中数据记录之间的映射关系的统称，是一种进行程序和数据库之间数据持久化的一种编程思想。
#Author:    smartwy
#Date:     
#Version:


from sqlalchemy import Column, String, Integer, ForeignKey, create_engine # 字段定义属性
from sqlalchemy.orm import sessionmaker,relationship # orm会话的创建,关联其它表
from sqlalchemy.ext.declarative import declarative_base #基础类封装

Base = declarative_base() # 创建基础类

class User(Base): # 暂时理解：把User映射到python表，在程序里操作User等于操作python
	# 定义与指定数据表之间的关联
	__tablename__ = 'python'
	# 创建字段类型 与数据库中字段相对应
	name = Column(String(20), primary_key=True) # 表结构的char对应程序中的Sting
	age = Column(Integer)
	sex = Column(String(1))
	tel = Column(String(11))
	school = relationship('School') # 关联其它表

	def __repr__(self): # 此方法自动执行，设置返回查询格式
		temp = '%s,%s,%s,%s' % (self.name, self.age, self.sex, self.tel)
		return  temp

class School(Base): # 此段代码只是示意关联其它表所写，
	__tablename__ = 'sch'
	# 创建字段类型 与数据库中字段相对应
	name = Column(String(20), primary_key=True)
	banji = Column(String(10))
	user_tel = Column(String(11), ForeignKey('python.tel'))  # 关联到其它表的那个字段

def main_function():
	# 数据库类型+数据库驱动名称://用户名:口令@机器地址:端口号/数据库名
	engine = create_engine('mysql+pymysql://root:12345678@192.168.12.66:3306/test')
	# 增删改查操作是通过一个session对象(DBSession,是由sessionmaker创建的)来完成的。
	DBseeeion = sessionmaker(bind=engine) # 创建会话，需要指定和那个数据库引擎之间的会话
	session = DBseeeion() # 使用session会话进行数据库操作了，暂时可以理解为mysql的游标cursor

	# new_user = User(name='zhangsan',tel='12110')
	# session.add(new_user) #增
	data = session.query(User).filter(User.tel=='10089').one() # 查
	# data.name = 'lisi' # 改
	# session.delete(data) # 删
	print('query : {}'.format(data)) # 因user类中定义了__repr__，所以可以返回自定义的格式而不是内存地址

	session.commit()
	session.close()
if __name__ == '__main__':
	main_function()


