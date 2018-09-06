# -*- coding:utf-8 -*-
#Name:     
#Descripton:
#Author:    smartwy
#Date:     
#Version:


# from PIL import Image,ImageFilter
#
# im = Image.open('tcpip.jpg') # 打开图片
# w, h = im.size  # 获取大小
# print('original w:%s h:%s'%(w,h))
# im.thumbnail((w//2,h//2))    # 缩小1/2
# print('display w:%s h:%s'%(w//2,h//2))
# im = im.convert('RGB')       # 有些图片需要转换模式 不然报错OSERROR
# im.save('a.jpg','jpeg')     # 保存图片
# im.show()                   #显示图片
# # im1 = im.filter(ImageFilter.BLUR) # 模糊图片
# # im1.save('tcpip1.jpg','jpeg')
# # Image.open('tcpip1.jpg').show()

# from PIL import Image,ImageFilter,ImageDraw,ImageFont
# import random
#
# def yanzheng():
# 	L = []
# 	def rndChar(): # 随机字母
# 		zimu = chr(random.randint(65, 90))
# 		L.append(zimu)
# 		return zimu
# 	def rndColor(): # 随机颜色1
# 		return (random.randint(32,127),random.randint(32,127),random.randint(32,127))
# 	def rndColor2(): # 随机颜色2
# 		return (random.randint(64,255),random.randint(64,255),random.randint(64,255))
# 	width = 60*4
# 	height = 60
# 	image = Image.new('RGB',(width,height),(255,255,255)) # 新建图像参数
# 	font = ImageFont.truetype('C:\Windows\Fonts\Arial.ttf',36)  # 创建对象，设置字体
# 	draw = ImageDraw.Draw(image)  # 创建绘制对象
# 	for i in range(width):  # 填充画布
# 		for j in range(height):
# 			draw.point((i,j),fill=rndColor())
# 	for i in range(4):  # 输出文字
# 		draw.text((60*i+10,10),rndChar(),font=font,fill=rndColor2())
# 	image = image.filter(ImageFilter.BLUR) # 模糊图片
# 	image.show()
# 	return L
# num1 = yanzheng()
# num = list(input('Please input image : ').upper())
# # num = [x.capitalize() for x in num]
# print(num1,num)
# if num == num1:
# 	print('ok')
# else:
# 	print('no')




# import requests,re

# r = requests.get('https://www.csdn.net/')
# print(r.status_code)
# print(r.headers)
# r = requests.get('https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20%3D%202151330&format=json')
# print(r.json())

# r = requests.get('https://www.douban.com/', headers={'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit'})
# print(re.search(r'\d{1,6}',r.text).group())
# print(r.text)

# import chardet
# '''
# 	检测未知编码的编码格式
# '''
# ji = chardet.detect(b'hello world !')
# print(ji['encoding'])
# print(ji)
#
# data = '小桥流水人家'.encode('utf-8')
# print(chardet.detect(data))
#
# data =  '最新の主要ニュース'.encode('euc-jp')
# print(chardet.detect(data))

import psutil,re

# c = psutil.cpu_count() # cpu逻辑数量
# print(c)
# c = psutil.cpu_count(logical=False) # cpu物理核心
# print(c)
# c = psutil.cpu_times()
# print(c)
# for x in range(10):
# 	print(psutil.cpu_percent(interval=1,percpu=True))

# mem = psutil.virtual_memory()
# print(mem)
# mem = psutil.swap_memory()
# print(mem)

# part = psutil.disk_partitions()
# print(part)
# part = psutil.disk_usage('/')
# print(part)
# part = psutil.disk_io_counters()
# print(part)

# net = psutil.net_connections()
# print(net)
# net = psutil.net_io_counters()
# print(net)
# net = psutil.net_if_addrs()
# print(str(net))
# nex = re.finditer(r'([0-9]{1,2}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3})', str(net))
# for i in nex:
# 	print(i.group())
# net = psutil.net_if_stats()
# print(net)
# net = psutil.net_if_stats()
# print(net)
# line = psutil.net_connections()
# print(line)
# it = psutil.pids()
# for i in it:
# 	print(psutil.Process(i))
# for x in ( psutil.Process(i).name() for i in psutil.pids()):
# 	print(x)

# print(psutil.test())
'''
virtualenv 可以在同一python版本下虚拟一套独立的python环境。
'''
