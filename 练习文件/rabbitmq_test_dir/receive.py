#!/usr/bin/python3
# -*- coding:utf-8 -*-
#P-Name:    python_test
#F-Name:    receive.py
#Login:     Administrator   
#Descripton:
#Author:    Smartwy
#Date:      2019/6/24 17:08:07
#Version:


import pika
import time
# 建立与mq的链接与队列
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()
# durable=True声明queue是持久化的，这样即便Rabb崩溃了重启后queue仍然存在其中的message不会丢失
channel.queue_declare(queue='m1', durable=True)

# ch，方法，属性，正文
def callback(ch, method, properties, body):
    # print(ch, method,properties, body,sep='\n')
    body = str(body, encoding='utf-8')
    time.sleep(10)
    print(" [x] Received %r" % body)
    ch.basic_ack(delivery_tag=method.delivery_tag) # 手动发送处理结束标签,接收下一个消息

#使用prefetch_count=1的basic_qos方法可告知RabbitMQ只有在消费者处理并确认了上一个message后才分配新的message给他
#否则分给另一个空闲的consumer
channel.basic_qos(prefetch_count=1)

# 接收设置，指定队列名称，及回调函数，auto_ack:自动回复mq服务已收到信息
channel.basic_consume(queue='m1', on_message_callback=callback)
print(' [*] Waiting for messages. To exit press CTRL+C')

# 一直等待消息到来，一直等，
channel.start_consuming()


