# -*- coding:utf-8 -*-
#Name:     
#Descripton:
#Author:    smartwy
#Date:     
#Version:

# import sqlite3
#
# sdb = sqlite3.connect('test.db')
# cursor = sdb.cursor()
# # sql = 'create table user (name char(20) not null primary key, age char(3), sex char(1),tel char(11))'
# # sql = "insert into user values ('wangye','18','m','10010')"
# # sql = 'drop table user'
# sql = 'select * from user'
# # name = input("Please input name :")
# # sql = "select * from user where name='%s'" % name # 占位符%s两侧必须有引号
# # for i in range(10):
# # 	sql = "insert into user values ('wangye%s','18','m','10010')" % i
# # 	cursor.execute(sql)
# try:
# 	cursor.execute(sql)
# 	sdb.commit()
# except:
# 	sdb.rollback()
# finally:
# 	print(cursor.fetchall(), cursor.rowcount)
# 	cursor.close()
# 	sdb.close()



import os, sqlite3

db_file = os.path.join(os.path.dirname(__file__), 'test1.db')
if os.path.isfile(db_file):
    os.remove(db_file)

# 初始数据:
conn = sqlite3.connect(db_file)
cursor = conn.cursor()
cursor.execute('create table user(id varchar(20) primary key, name varchar(20), score int)')
cursor.execute(r"insert into user values ('A-001', 'Adam', 95)")
cursor.execute(r"insert into user values ('A-002', 'Bart', 62)")
cursor.execute(r"insert into user values ('A-003', 'Lisa', 78)")


def get_score_in(low, high):
    # 查询分数区间，并升序排列
    cursor.execute("select name from user where score >= %d and score <= %d ORDER BY score ASC" % (low, high))
    return cursor.fetchall()
# 测试:
assert get_score_in(80, 95) == [('Adam',)], get_score_in(80, 95)
assert get_score_in(60, 80) == [('Bart',), ('Lisa',)], get_score_in(60, 80)
assert get_score_in(60, 100) == [('Bart',), ('Lisa',), ('Adam',)], get_score_in(60, 100)
# dd = get_score_in(80, 95)
print(get_score_in(60, 100))
cursor.close()
conn.commit()
conn.close()

print(os.path.join(os.path.dirname(__file__), 'test1.db'))
