# -*- coding:utf-8 -*-
#Name:     
#Descripton:
#Author:    smartwy
#Date:     
#Version:

import threading,time


# def loop():
# 	print('thread %s is running...'%threading.current_thread().name)
# 	n = 0
# 	while n < 5:
# 		n += 1
# 		print('thread %s >>> %s '%(threading.current_thread().name,n))
# 		time.sleep(1)
# 	print('thread %s ended.'%threading.current_thread().name)       # current_thread() 返回当前线程实例
# print('thread %s running...'% threading.current_thread().name)
# t = threading.Thread(target=loop,name='loopthread')
# t.start()
# t.join()
# print('thread %s ended'%threading.current_thread().name)

balance = 0
lock = threading.Lock()     # 创建一个锁
def change_it(n):
    # 先存后取，结果应该为0:
    # print(n)
    global balance
    balance = balance + n +1
    balance = balance - n

def run_thread(n):
    for i in range(100000):
        # change_it(n)
        lock.acquire()      # 获取锁
        try:
            change_it(n)
        finally:
            lock.release()  # 释放锁
    # print(threading.current_thread())

t1 = threading.Thread(target=run_thread, args=(5,))
t2 = threading.Thread(target=run_thread, args=(8,))
t1.start()
t2.start()
t1.join()
t2.join()
print(balance)

# 全局解释器锁（GIL） 正因为这个锁，保证同一时刻只有一个线程在执行。
# 在多线程环境中，Python 虚拟机按以下方式执行：
# 1. 设置GIL
# 2. 切换到一个线程去运行
# 3. 运行：
#     a. 指定数量的字节码指令，或者
#     b. 线程主动让出控制（可以调用time.sleep(0)）
# 4. 把线程设置为睡眠状态
# 5. 解锁GIL
# 6. 再次重复以上所有步骤
#  Python虽然不能利用多线程实现多核任务，但可以通过多进程实现多核任务，多个Python进程有各自独立的GIL锁，互不影响。

# def test1():
# 	print('start test1')
# 	time.sleep(10)
# 	print('******stop test1')
# def test2():
# 	print('start test2')
# 	time.sleep(10)
# 	print('******stop test2')
# def test3():
# 	print('start test3')
# 	time.sleep(10)
# 	print('*******stop test3')
# if __name__ == '__main__':
# 	t1 = threading.Thread(target=test1())
# 	t2 = threading.Thread(target=test2())
# 	t3 = threading.Thread(target=test3())
# 	t1.start()
# 	t2.start()
# 	t3.start()
# 	t1.join()
# 	t2.join()
# 	t3.join()
