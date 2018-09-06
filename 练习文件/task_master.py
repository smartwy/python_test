# -*- coding:utf-8 -*-
#Name:     
#Descripton:
#Author:    smartwy
#Date:     
#Version:

# import random,time,queue,
# from multiprocessing.managers import BaseManager
#
# task_queue = queue.Queue()     # 发送任务队列
# result_queue = queue.Queue()    # 接受结果队列
#
# class QueueManager(BaseManager): # 继承BaseManager
# 	pass
# QueueManager.register('get_task_queue',callable=lambda: task_queue)  # 注册queue到网络，callable参数关联queue对象
# QueueManager.register('get_result_queue',callable=lambda: result_queue)
# manager = QueueManager(address=('',5000),authkey=b'abc')   # 绑定端口，设置验证码
# manager.start()    # 启动queue
# task = manager.get_task_queue()   # 关联网络的queue对象
# result = manager.get_result_queue()
# # 放几个任务进去:
# for i in range(10):
#     n = random.randint(0, 10000)
#     print('Put task %d...' % n)
#     task.put(n)
# # 从result队列读取结果:
# print('Try get results...')
# for i in range(10):
#     r = result.get(timeout=10)
#     print('Result: %s' % r)
# # 关闭:
# manager.shutdown()
# print('master exit.')



