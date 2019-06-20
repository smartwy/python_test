#!/usr/bin/python3
# -*- coding:utf-8 -*-
#P-Name:    python_test
#F-Name:    matplotlib_pro.py
#Login:     Administrator   
#Descripton:
#Author:    Smartwy
#Date:      2019/2/20 18:50:22
#Version:

# import numpy as np
# from matplotlib import pyplot as pt
#
# x = np.arange(1,11)
# y = 2*x+5
# pt.title('matplotlib test')
# pt.xlabel('x ')
# pt.ylabel('y ')
# pt.plot(x,y,'or')
# pt.show()

# import numpy as np
# import matplotlib.pyplot as plt
# # 计算正弦曲线上点的 x 和 y 坐标
# x = np.arange(0,  3  * np.pi,  0.1)
# y = np.sin(x)
# plt.title("sine wave form")
# # 使用 matplotlib 来绘制点
# plt.plot(x, y)
# plt.show()


# from matplotlib import pyplot as plt
# x =  [5,8,10]
# y =  [12,16,6]
# x2 =  [6,9,11]
# y2 =  [6,15,7]
# plt.bar(x, y, align =  'center')
# plt.bar(x2, y2, color =  'g', align =  'center')
# plt.title('Bar graph')
# plt.ylabel('Y axis')
# plt.xlabel('X axis')
# plt.show()


# # 导入 matplotlib 的所有内容（nympy 可以用 np 这个名字来使用）
# from pylab import *
#
# # 创建一个 8 * 6 点（point）的图，并设置分辨率为 80
# figure(figsize=(8,6), dpi=80)
#
# # 创建一个新的 1 * 1 的子图，接下来的图样绘制在其中的第 1 块（也是唯一的一块）
# subplot(1,1,1)
#
# X = np.linspace(-np.pi, np.pi, 256,endpoint=True)
# C,S = np.cos(X), np.sin(X)
# # C,S = np.tan(X), np.sin(X)
# # 绘制余弦曲线，使用蓝色的、连续的、宽度为 1 （像素）的线条
# plot(X, C, color="blue", linewidth=5.0, linestyle="-")
#
# # 绘制正弦曲线，使用绿色的、连续的、宽度为 1 （像素）的线条
# plot(X, S, color="green", linewidth=1.0, linestyle="-")
#
# # 设置横轴的上下限
# xlim(-4.0,4.0)
#
# # 设置横轴记号
# xticks(np.linspace(-4,4,9,endpoint=True))

# # 设置纵轴的上下限
# ylim(-1.0,1.0)
#
# # 设置纵轴记号
# yticks(np.linspace(-1,1,5,endpoint=True))
#
# # 以分辨率 72 来保存图片
# # savefig("exercice_2.png",dpi=72)
#
# # 在屏幕上显示
# show()


# import matplotlib.pyplot as plt
# import psutil
# for i in range(5):
# 	# plt.clf()
# 	plt.plot([ i for j in range(6) for i in [-1,4,7,5,-4,6,2,6,4,9]])
# 	plt.ylabel('y')
# 	plt.xlabel('x')
# 	# plt.axes(-10,10,0,60)
# 	re = psutil.net_io_counters().bytes_recv
# 	se = psutil.net_io_counters().bytes_sent
# 	plt.ylim(0,144)
# 	# plt.xlim(0,60)
# 	# plt.savefig('img', dpi=600)
# 	plt.show()


# from matplotlib import pyplot as plt
# import numpy as np
#
# x = np.linspace(1, 100, 20)
# y = x * 2 + 3
# fig = plt.figure()
# ax = fig.add_subplot(1, 1, 1)
# ax.scatter(x, y)
# plt.ion()
# for i in range(10):
# 	y = x * i * 0.1 + i
# 	try:
# 		ax.lines.remove(lines[0])
# 	except Exception:
# 		pass
# 	lines = ax.plot(x, y)
# 	plt.pause(0.1)


# import matplotlib.pyplot as plt
# import numpy as np
# import time
# from math import *
#
# plt.ion() #开启interactive mode 成功的关键函数
# plt.figure(1)
# t = [0]
# t_now = 0
# m = [sin(t_now)]
#
# for i in range(2000):
# 	# plt.clf() # 清空画布上的所有内容。此处不能调用此函数，不然之前画出的点，将会被清空。
#     t_now = i*0.1
#     """
#     由于第次只画一个点，所以此处有两种方式，第一种plot函数中的样式选
#     为点'.'、'o'、'*'都可以，就是不能为线段'-'。因为一条线段需要两
#     个点才能确定。第二种方法是scatter函数，也即画点。
#     """
#     plt.plot(t_now,sin(t_now),'.') # 第次对画布添加一个点，覆盖式的。
#     # plt.scatter(t_now, sin(t_now))
#
#     plt.draw()#注意此函数需要调用
#     time.sleep(0.01)


# import matplotlib.pyplot as plt
# import numpy as np
# import time
# from math import *
# import psutil
# plt.ion()  # 开启interactive mode 成功的关键函数
# plt.figure(1)
# # t = np.linspace(0, 20, 100)
#
# for i in range(20):
# 	# plt.clf() # 清空画布上的所有内容。此处不能调用此函数，不然之前画出的轨迹，将会被清空。
# 	# y = np.sin(t * i / 10.0)
# 	t = 124
# 	y = 423
# 	plt.plot(t, y)  # 一条轨迹
# 	plt.draw()  # 注意此函数需要调用
# 	time.sleep(1)



# import math
# import random
# import numpy as np
# import matplotlib
# import matplotlib.pyplot as plt
#
# import psutil
#
# # set up matplotlib
# is_ipython = 'inline' in matplotlib.get_backend()
# if is_ipython:
# 	from IPython import display
# plt.ion()
#
# def plot_durations(y):
# 	plt.figure(1) # plt.figure(1)是新建一个名叫 Figure1的画图窗口，
# 	plt.clf() # 清空画布内容
# 	plt.subplot(211) # 图形绘图区域，211：第一整行，212：第二整行，221：第一行左图，222：第一行右图.131,132,133
# 	plt.plot(y[:, 0]) # plt.plot(x,c)是在画图窗口里具体绘制横轴为x 纵轴为c的曲线
# 	plt.subplot(212) # subplot(nrows, ncols, plot_number),
# 					# nrows和ncols表示将画布分成（nrows*ncols）个小区域，
# 					# 每个小区域可以单独绘制图形；plot_number表示将图绘制在第plot_number个子区域。
# 	plt.plot(y[:, 1])
#
# 	plt.pause(1)  # pause a bit so that plots are updated
# 	if is_ipython:
# 		display.clear_output(wait=True)
# 		display.display(plt.gcf())
#
# x = np.linspace(-10, 10, 500)
# y = []
# for i in range(len(x)):
# 	# y1 = np.cos(i / (3 * 3.14))
# 	y1 = psutil.net_io_counters().bytes_recv/1024/1024
# 	# y2 = np.sin(i / (3 * 3.14))
# 	y2 = psutil.net_io_counters().bytes_sent/1024/1024
# 	y.append(np.array([y1, y2]))  # 保存历史数据
# 	plot_durations(np.array(y))


#
# import math
#
# import numpy as np
# import matplotlib.pyplot as plt
# from matplotlib.animation import FuncAnimation
#
#
# def beta_pdf(x, a, b):
#     return (x**(a-1) * (1-x)**(b-1) * math.gamma(a + b)
#             / (math.gamma(a) * math.gamma(b)))
#
#
# class UpdateDist(object):
#     def __init__(self, ax, prob=0.5):
#         self.success = 0
#         self.prob = prob
#         self.line, = ax.plot([], [], 'k-')
#         self.x = np.linspace(0, 1, 200)
#         self.ax = ax
#
#         # Set up plot parameters
#         self.ax.set_xlim(0, 1)
#         self.ax.set_ylim(0, 15)
#         self.ax.grid(True)
#
#         # This vertical line represents the theoretical value, to
#         # which the plotted distribution should converge.
#         self.ax.axvline(prob, linestyle='--', color='black')
#
#     def init(self):
#         self.success = 0
#         self.line.set_data([], [])
#         return self.line,
#
#     def __call__(self, i):
#         # This way the plot can continuously run and we just keep
#         # watching new realizations of the process
#         if i == 0:
#             return self.init()
#
#         # Choose success based on exceed a threshold with a uniform pick
#         if np.random.rand(1,) < self.prob:
#             self.success += 1
#         y = beta_pdf(self.x, self.success + 1, (i - self.success) + 1)
#         self.line.set_data(self.x, y)
#         return self.line,
#
# # Fixing random state for reproducibility
# np.random.seed(19680801)
#
#
# fig, ax = plt.subplots()
# ud = UpdateDist(ax, prob=0.7)
# anim = FuncAnimation(fig, ud, frames=np.arange(100), init_func=ud.init,
#                      interval=5, blit=True)
# plt.show()


#
# import matplotlib.pyplot as plt
# import numpy as np

# x = np.arange(0,5,0.1)
# y = np.sin(x)
# plt.plot(x,y)
# plt.axis((0,7,-2,2))
# plt.show()




# plt.figure('windows 1',figsize=(10,6),dpi=80) # 设置画布
# data = {'a': np.arange(50),
#         'c': np.random.randint(0, 50, 50),
#         'd': np.random.randn(50)}
# # print(data)
# data['b'] = data['a'] + 10 * np.random.randn(50)
# data['d'] = np.abs(data['d']) * 100
# # print(data)
# plt.subplot(131) # 第一行三个位置第一个位置 131
# plt.scatter('a', 'b', c='c', s='d', data=data) # 生成散点图
#
# plt.subplot(132) # 第一行三个位置第二个位置 132
# plt.plot(data['a'],data['b'], 'r+') # 生成曲线图
#
# plt.subplot(133) # 第一行三个位置第三个位置 133
# plt.bar(data['a'],data['b']) # 生成条状图
#
# plt.xlabel('entry a')
# plt.ylabel('entry b')
# plt.suptitle('tables head ！')
# plt.savefig('a-a')
# plt.show()


import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button, RadioButtons

fig, ax = plt.subplots()
plt.subplots_adjust(left=0.25, bottom=0.25)
t = np.arange(0.0, 1.0, 0.001)
a0 = 5
f0 = 3
delta_f = 5.0
s = a0*np.sin(2*np.pi*f0*t)
l, = plt.plot(t, s, lw=2, color='red')
plt.axis([0, 1, -10, 10])

axcolor = 'lightgoldenrodyellow'
axfreq = plt.axes([0.25, 0.1, 0.65, 0.03], facecolor=axcolor)
axamp = plt.axes([0.25, 0.15, 0.65, 0.03], facecolor=axcolor)

sfreq = Slider(axfreq, 'Freq', 0.1, 30.0, valinit=f0, valstep=delta_f)
samp = Slider(axamp, 'Amp', 0.1, 10.0, valinit=a0)


def update(val):
    amp = samp.val
    freq = sfreq.val
    l.set_ydata(amp*np.sin(2*np.pi*freq*t))
    fig.canvas.draw_idle()
sfreq.on_changed(update)
samp.on_changed(update)

resetax = plt.axes([0.8, 0.025, 0.1, 0.04])
button = Button(resetax, 'Reset', color=axcolor, hovercolor='0.975')


def reset(event):
    sfreq.reset()
    samp.reset()
button.on_clicked(reset)

rax = plt.axes([0.025, 0.5, 0.15, 0.15], facecolor=axcolor)
radio = RadioButtons(rax, ('red', 'blue', 'green'), active=0)


def colorfunc(label):
    l.set_color(label)
    fig.canvas.draw_idle()
radio.on_clicked(colorfunc)

plt.show()