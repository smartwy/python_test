# -*- coding:utf-8 -*-
#Name:     
#Descripton:
#Author:    smartwy
#Date:     
#Version:

import os

# print('Process (%s) start ...'%os.getpid())
#
# pid = os.fork()         # windows 没有fork调用，linux unix Mac支持fork调用
#
# if pid == 0:
# 	print('I am child process (%s) and my parent is %s .'%(os.getpid(),os.getppid()))
# else:
# 	print("I (%s) just created a child process (%s)."%(os.getpid(),pid))

from multiprocessing import Process
from multiprocessing import Pool
import os
import time,random

# def run_proc(name):
# 	print('Run child process name:%s (id:%s) ...'%(name,os.getpid()))
# 	# time.sleep(20)
# 	for i in range(3):
# 		# print(i)
# 		time.sleep(1)
#
# if __name__ == '__main__':
# 	print('Parent process %s'%os.getpid())
# 	argsl = ['a','n', 'o', 'e']
# 	for i in argsl:
# 		p = Process(target=run_proc,args=(i,))
# 		print('Child process will start')
# 		p.start()        # 启动子进程，
# 	p.join()            # join方法可以等子进程结束后继续往下执行，通常用于进程间的同步
# 						# 如果不使用join()启动完全部子进程后不会等待进程结束，直接往下执行
# 	print('Child process end')

def long_time_task(name):
    print('Run process %s task %s ...' % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print('Task %s runs %0.2f seconds.' % (name, (end - start)))

if __name__=='__main__':
    print('Parent process {}.'.format(os.getpid()))
    p = Pool(4)
    for i in range(6): #  进程池最多4个进程，这里放了6个，则先执行4个，结束一个启动一个，直到6个全部执行完
        p.apply_async(long_time_task, args=(i,))
    print('Waiting for all subprocesses done...')
    p.close()           # 调用close之后不能添加新的进程了
    p.join()            # 等待所有子进程执行完毕再往下执行，否则直接往下执行
    print('All subprocesses done.')
    # p.apply_async(long_time_task,args=('wy')) 放在了close()之后，报错

# from multiprocessing import Value
#
# print(money)







