#!/usr/bin/python3
# -*- coding:utf-8 -*-
#P-Name:    python_test
#F-Name:    线程同步.py
#Login:     Administrator   
#Descripton:
#Author:    Smartwy
#Date:      2017/6/20 14:44:13
#Version:

# 主线程与子线程生命周期同步
import threading
import time

# # 1 默认情况下就是setDaemon(False),主线程执行完自己的任务以后退出，此时子线程会继续执行自己的任务，直到自己的任务结束。
def thread():
    time.sleep(2)
    print('---子线程结束---')

def main():
    t1 = threading.Thread(target=thread)
    t1.start()
    print('---主线程--结束')

if __name__ =='__main__':
    main()

# 2 当我们使用setDaemon(True)时，这是子线程为守护线程，主线程一旦执行结束，则全部子线程被强制终止
def thread():
    time.sleep(2)
    print('---子线程结束---')
def main():
    t1 = threading.Thread(target=thread)
    t1.setDaemon(True) # 设置子线程守护主线程，主线程代码全部执行完毕，子线程也会跟随强制结束，主死 子死
    t1.start()
    # time.sleep(3)
    print('---主线程结束---')

if __name__ =='__main__':
    main()

# 3
def thread():
    time.sleep(2)
    print('---子线程结束---')
def main():
    for _ in range(5):
        t1 = threading.Thread(target=thread)
        t1.setDaemon(True) # 设置子线程为守护线程
        t1.start()
        # time.sleep(2)
        t1.join(timeout=2)#1 不设timeout 主线程阻塞当前位置，子线程结束后再继续执行后续代码
                       #2 如果设置了setDaemon=True和timeout=1,主线程等待1s后会强制杀死子线程，然后主线程结束
                       #3 如果子线程执行时间少于timeout时间，那么子线程结束后主线程便直接往下执行，无需等待timeout时间终止
    print('---主线程结束---')

if __name__=='__main__':
    main()


