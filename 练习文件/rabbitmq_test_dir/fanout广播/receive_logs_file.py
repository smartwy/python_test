#!/usr/bin/python3
# -*- coding:utf-8 -*-
#P-Name:    python_test
#F-Name:    receive_logs.py
#Login:     Administrator   
#Descripton:
#Author:    Smartwy
#Date:      2019/6/25 15:03:40
#Version:
# 日志消息接收者：建立连接，声明exchange，将exchange与queue进行绑定，开始不停的接收log并打印。

import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

#此处定义一个名称为'logs'的'fanout'类型的exchange，两个程序只需一个声明，为了保证一定存在，所以两个程序均声明
channel.exchange_declare(exchange='logs', exchange_type='fanout')

#将exclusive置为True，这样在消防者从RabbitMQ断开后会删除该queue，这样的队列具有时效性：过期不候
result = channel.queue_declare(queue='', exclusive=True)
queue_name = result.method.queue

#exchange与queue之间的关系成为binding
#binding告诉exchange将message发送该哪些queue
channel.queue_bind(exchange='logs', queue=queue_name)

print('Waiting for logs write to file.')

def callback(ch, methon, properties, body):
	with open('recerve_logs.txt','a') as f:
		f.write(str(body, encoding='utf-8')+'\n')
	print('Write file ok !')

channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)

channel.start_consuming()



