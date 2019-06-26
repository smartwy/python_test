#!/usr/bin/python3
# -*- coding:utf-8 -*-
#P-Name:    python_test
#F-Name:    receive_logs_topic.py
#Login:     Administrator   
#Descripton:
#Author:    Smartwy
#Date:      2019/6/26 11:22:01
#Version:

# 调用接收时使用字符串与*/#来匹配一个单词或0个多个单词

import pika
import sys

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='topic_logs', exchange_type='topic')

result = channel.queue_declare(queue='', exclusive=True)
queue_name = result.method.queue

binding_keys = sys.argv[1:]
if not binding_keys:
    sys.stderr.write("Usage: %s [binding_key]...\n" % sys.argv[0])
    sys.exit(1)

for binding_key in binding_keys:
    channel.queue_bind(
        exchange='topic_logs', queue=queue_name, routing_key=binding_key)

print(' [*] Waiting for logs. To exit press CTRL+C')

def callback(ch, method, properties, body):
    print(" [x] %r:%r" % (method.routing_key, body))

channel.basic_consume(
    queue=queue_name, on_message_callback=callback, auto_ack=True)

channel.start_consuming()

# 接收queue时使用：Python receive_logs_topic.py 'wy.*' 说明：只接收是wy.后面有一个词的routing_key
#                 Python receive_logs_topic.py 'wy.#' 说明：只接收是wy.开头的routing_key
#                 Python receive_logs_topic.py 'wy.*.info' 说明：只接收三个单词且前后两词为wy,info的routing_key
#                 Python receive_logs_topic.py 'wy.#.info' 说明：只接收前后两词为wy,info的routing_key
# 有点像通配符
