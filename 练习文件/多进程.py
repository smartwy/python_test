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
# 	print('Run child process %s (%s) ...'%(name,os.getpid()))
# 	# time.sleep(20)
# 	for i in range(5):
# 		print(i)
# 		time.sleep(1)
#
# if __name__ == '__main__':
# 	print('Parent process %s'%os.getpid())
# 	p = Process(target=run_proc,args=('test',))
# 	print('Child process will start')
# 	p.start()
# 	print('test')
# 	p.join()            # join方法可以等子进程结束后继续往下执行，通常用于进程间的同步
# 	print('Child process end')
#
def long_time_task(name):
    print('Run task %s (%s)...' % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print('Task %s runs %0.2f seconds.' % (name, (end - start)))

if __name__=='__main__':
    print('Parent process %s.' % os.getpid())
    p = Pool(4)
    for i in range(5):
        p.apply_async(long_time_task, args=(i,))
    print('Waiting for all subprocesses done...')
    p.close()           # 调用close之后不能添加新的进程了
    p.join()            # 等待所有子进程执行完毕
    print('All subprocesses done.')
    # p.apply(long_time_task,args=('wy')) 放在了close()之后，报错









