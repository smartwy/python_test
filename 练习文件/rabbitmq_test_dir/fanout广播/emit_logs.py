#!/usr/bin/python3
# -*- coding:utf-8 -*-
#P-Name:    python_test
#F-Name:    emit_logs.py
#Login:     Administrator   
#Descripton:
#Author:    Smartwy
#Date:      2019/6/25 15:11:22
#Version:
# 日志消息发送者：建立连接，声明fanout类型的exchange，通过exchage向queue发送日志消息，消息被广播给所有接收者，关闭连接，退出。

import pika
import time

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

#此处定义一个名称为'logs'的'fanout'类型的exchange，'fanout'类型的exchange简单的将message广播到它所知道的所有queue
channel.exchange_declare(exchange='logs', exchange_type='fanout')

message = '{} -> This is a one logs '.format(time.strftime('%Y-%m-%d %H-%M-%S'))
# 发布消息
channel.basic_publish(exchange='logs', routing_key='', body=message)
print(message)
connection.close()


