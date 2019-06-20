# -*- coding:utf-8 -*-
#Name:     
#Descripton:
#Author:    smartwy
#Date:     
#Version:


# 协程，可以理解是进程和线程的升级版，进程和线程都有内核态和用户态切换的问题，而协程是自己控制切换
def consumer(name):
    print('开始吃包子...')
    while True:
        print('\033[31;1m[consumer]%s需要包子\033[0m'%name)
        bone = yield   # 接收send发送的数据
        print('\033[31;1m[%s]吃了%s个包子\033[0m'%(name,bone))

def producer(obj1):
    obj1.send(None)   # 和next方法一样 获取下一个值，必须先使用None参数调用一次， 执行到yield
    for i in range(1,10,3):
        print('\033[32;1m[producer]\033[0m正在做%s个包子'%i)
        obj1.send(i)
    print(obj1,type(obj1))
    obj1.close()

if __name__ == '__main__':
    con1 = consumer('消费者A')  #创建消费者对象
    producer(con1)




