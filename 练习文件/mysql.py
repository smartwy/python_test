# -*- coding:utf-8 -*-
#Name:     
#Descripton:
#Author:    smartwy
#Date:     
#Version:


import pymysql
data = []
db = pymysql.connect('10.130.228.30', 'root', 'password', 'test', port=3306)
cursor = db.cursor() # 创建数据库游标
sql = 'select * from python'
# sql = '''
# 		create table python (
# 		name char(20) not null primary key,
# 		age int,
# 		sex char(1),
# 		tel char(11))
# 	'''
# sql = 'create table sch (name char(20) not null primary key, banji char(10), user_tel char(10))'
# sql = 'drop table python'
# name,age,sex,tel = input('Please input name,age,sex,tel  : ').split() # 以，分切输入的数据，缺省默认空格
# sql = "insert into python values ('%s','%s','%s','%s')" % (name,age,sex,tel)
# sql = "update python set age = age+10 where sex = '%c'" % 'm'
# sql = 'select * from python where age >10'
try:
	cursor.execute(sql) # 执行sql语句
	data = cursor.fetchall() # 接收全部数据，fetchone()接收单条数据
	db.commit() # 真正提交到数据 防止提交失败，可在execpt内添加rollback()回滚所有操作
except :
	print("ERROR ! Please check sql !")
	db.rollback() # 回滚
finally:
	# pass
	# if not data:
	# 	print('sql exec error !')
	# else:
	print(data)
cursor.close()
db.close() # 关闭数据库


