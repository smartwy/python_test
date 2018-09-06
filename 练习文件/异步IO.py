# -*- coding:utf-8 -*-
#Name:     
#Descripton:
#Author:    smartwy
#Date:     
#Version:


# import asyncio
# import threading
#
# @asyncio.coroutine
# def hello():
# 	i = 0
# 	print("Hello world! %s " % threading.current_thread())
# 	yield from asyncio.sleep(5) # 模拟IO
# 	print("Hello again! %s " % threading.current_thread())
#
# # 获取EventLoop:
# loop = asyncio.get_event_loop()
# # 执行coroutine
# tasks = [hello(), hello()]
# loop.run_until_complete(asyncio.wait(tasks)) # 把两个任务都放在EventLoop中执行
# loop.close()
#
# # 根据输出，两个协同程序由一个线程并发执行，把sleep()换乘真正的IO操作，则多个coroutine就可以由一个线程并发执行

'''*********************************************************************************************'''

# # 使用async与await针对coroutine新语法
# import asyncio
#
# # @asyncio.coroutine
# # def hello():
# #     print('Hello world !')
# #     yield from asyncio.sleep(2)
# #     print('hello again !')
#
# async def hello():
#     print("hello WORLD")
#     await asyncio.sleep(2)
#     print("hello again")
#
# loop = asyncio.get_event_loop()
# tasks = [hello(),hello()]
# loop.run_until_complete(asyncio.wait(tasks))
# loop.close()

'''*********************************************************************************************'''

import asyncio
'''
	yield from 暂时可以理解为：后面跟可迭代对象形成生成器嵌套
'''
# @asyncio.coroutine
# def wget(host): # 实现异步网络
async def wget(host):  # 实现异步网络
    print('\033[0;31;40m wget %s...\033[0m' % host)
    connect = asyncio.open_connection(host, 80)
    # reader:流读出器、writer：流写入器，后续操作这两对象进行操作
    # reader, writer = yield from connect   # yield from 后面需要加的是可迭代对象，它可以是普通的可迭代对象，也可以是迭代器，甚至是生成器。 实现生成器嵌套
    reader, writer = await connect
    print('test---- %s...' % host)
    header = 'GET / HTTP/1.0\r\nHost: %s\r\n\r\n' % host
    writer.write(header.encode('utf-8')) # 类似socket.send()
    # yield from writer.drain() # 防止buffer溢出，及时把数据从缓冲区发送出去，async知道发送到哪 此例buffer是充足的
    await writer.drain()
    while True:
        # line = yield from reader.readline() # 从流读出器读出每行数据
        line = await reader.readline()
        if line == b'\r\n':
            break
        print('%s header > %s' % (host, line.decode('utf-8').rstrip()))
    # 只处理头信息，不处理主题
    writer.close()

loop = asyncio.get_event_loop()
tasks = [wget(host) for host in ['www.sina.com.cn', 'www.sohu.com', 'www.163.com']]
loop.run_until_complete(asyncio.wait(tasks)) # 并发三个任务
loop.close()