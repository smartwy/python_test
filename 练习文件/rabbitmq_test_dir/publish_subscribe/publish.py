#!/usr/bin/python3
# -*- coding:utf-8 -*-
#P-Name:    python_test
#F-Name:    publish.py
#Login:     Administrator   
#Descripton:
#Author:    Smartwy
#Date:      2019/6/25 21:03:34
#Version:

import pika
import sys

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

#此处定义一个名称为'direct_logs'的'direct'类型的exchange，'direct'类型的exchange将message根据routing_key发布到订阅者的queue
channel.exchange_declare(exchange='direct_logs', exchange_type='direct')

# 自定义routing_key，需要和订阅者约定好，都有哪几种key
severity = sys.argv[1] if len(sys.argv) > 1 else 'info'
message = ' '.join(sys.argv[2:]) or 'hello world!'

channel.basic_publish(exchange='direct_logs', routing_key=severity, body=message)

print('[*] {}: {}'.format(severity, message))

connection.close()



