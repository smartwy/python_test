# -*- coding:utf-8 -*-
#Name:     
#Descripton:
#Author:    smartwy
#Date:     
#Version:


from threading import Thread
import time
# # 单线程
def my_counter():
	i = 0
	print()
	for _ in range(1000000):
		i = i + 1
	return True

def main():
	# thread_array = {}
	start_time = time.time()
	for tid in range(2):
		t = Thread(target=my_counter)
		t.start()
		t.join()
	end_time = time.time()
	print(" 1 thread Total time: {}".format(end_time - start_time))

# if __name__ == '__main__':
# 	main()

# 并发双线程
def my_counter2():
	i = 0
	for _ in range(100000000):
		i = i + 1
	return True


def main2():
	thread_array = {}
	start_time = time.time()
	for tid in range(2):
		t = Thread(target=my_counter2)
		t.start()
		thread_array[tid] = t
	for i in range(2):
		thread_array[i].join()
	end_time = time.time()
	print("2 thread Total time: {}".format(end_time - start_time))


if __name__ == '__main__':
	main()
	# main2()
