#!/usr/bin/python3
# -*- coding:utf-8 -*-
#P-Name:    python_test
#F-Name:    send.py
#Login:     Administrator
#Descripton:
#Author:    Smartwy
#Date:      2019/6/24 16:51:03
#Version:

import pika
import sys
import time
import random
n = 0

# 链接mq 服务，host,port,user,password
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
# 创建队列
channel = connection.channel()

# 声明队列名称,durable=True声明queue是持久化的，这样即便Rabb崩溃了重启后queue仍然存在其中的message不会丢失
channel.queue_declare(queue='m1', durable=True)
while n < 8:
	# 发送数据，routing_key:队列名称/管道名称，body：数据,   执行文件时跟着的参数:''.join(sys.argv[1:])
	messages = 'This is the {} data。'.format(n)
	print(messages)
	# 发布消息
	channel.basic_publish(
		exchange='',
		routing_key='m1',
		body=messages,
		properties=pika.BasicProperties(
			delivery_mode=2, # 信息持久化，生产者消息在mq服务端存着，只要有对应的消费者在线再发送
		))
	# time.sleep(1)
	n += 1
# 除了要声明queue是持久化的外，还需声明message是持久化的
# basic_publish的properties参数指定message的属性
# 此处pika.BasicProperties中的delivery_mode=2指明message为持久的
# 这样一来RabbitMQ崩溃重启后queue仍然存在其中的message也仍然存在
# 需注意的是将message标记为持久的并不能完全保证message不丢失，因为
# 从RabbitMQ接收到message到将其存储到disk仍需一段时间，若此时RabbitMQ崩溃则message会丢失
# 况且RabbitMQ不会对每条message做fsync动作
# 可通过publisher confirms实现更强壮的持久性保证

# 关闭链接
connection.close()



