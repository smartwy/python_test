#!/usr/bin/python3
# -*- coding:utf-8 -*-
#P-Name:    python_test
#F-Name:    管道pipe.py
#Login:     Administrator   
#Descripton:
#Author:    Smartwy
#Date:      2019/2/25 16:24:32
#Version:
import time
# Queue和pipe只是实现了数据交互，并没实现数据共享，即一个进程去更改另一个进程的数据。
from multiprocessing import Process, Pipe


def f(conn):
	conn.send([12, {"name": "xyp"}, 'hello'])
	response = conn.recv()
	print("response", response)
	conn.close()
	print("q_ID2:", id(conn))

if __name__ == '__main__':
	parent_conn, child_conn = Pipe()
	print("q_ID1:", id(child_conn))
	p = Process(target=f, args=(child_conn,))
	p.start()
	print(parent_conn.recv())  # prints "[42, None, 'hello']"
	parent_conn.send("儿子你好!")
	p.join()

