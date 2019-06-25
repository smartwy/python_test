#!/usr/bin/python3
# -*- coding:utf-8 -*-
#P-Name:    python_test
#F-Name:    subscribe.py
#Login:     Administrator   
#Descripton:
#Author:    Smartwy
#Date:      2019/6/25 21:03:46
#Version:


import pika
import sys

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='direct_logs', exchange_type='direct')
#将exclusive置为True，这样在消防者从RabbitMQ断开后会删除该queue，这样的队列具有时效性：过期不候

result = channel.queue_declare(queue='', exclusive=True)
queue_name = result.method.queue

res = sys.argv[1:]

if not res:
	sys.stderr.write('Usage:%s info/warning/error\n'%sys.argv[0])
	sys.exit(1)

# 根据第一个参数来确定订阅的信息
# exchange和queue之间的binding可接受routing_key参数
# fanout类型的exchange直接忽略routing_key参数
# direct类型的exchange精确匹配该关键字进行message路由
# 对多个queue使用相同的binding_key是合法的
for severity in res:
	channel.queue_bind(exchange='direct_logs', queue=queue_name, routing_key=severity)

def func1(ch, method, properties, body):
	print('message:{}'.format(body))

channel.basic_consume(queue=queue_name, on_message_callback=func1, auto_ack=True)

channel.start_consuming()






