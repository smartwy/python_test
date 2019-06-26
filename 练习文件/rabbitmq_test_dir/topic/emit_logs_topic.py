#!/usr/bin/python3
# -*- coding:utf-8 -*-
#P-Name:    python_test
#F-Name:    emit_logs_topic.py
#Login:     Administrator   
#Descripton:
#Author:    Smartwy
#Date:      2019/6/26 11:22:14
#Version:


import pika
import sys

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

# 声明名为topic_logs的topic类型的exchange,
# topic类型的exchange可通过通配符对message进行匹配从而路由至不同queue
channel.exchange_declare(exchange='topic_logs', exchange_type='topic')

# 配置routing_key，message，
routing_key = sys.argv[1] if len(sys.argv) > 2 else 'smartwy.info'
message = ' '.join(sys.argv[2:]) or 'Hello World!'
# 发布
channel.basic_publish(
    exchange='topic_logs',
	routing_key=routing_key,
	body=message,
	)
print(" [x] Sent %r:%r" % (routing_key, message))

connection.close()


