# -*- coding:utf-8 -*-
#Name:     
#Descripton:
#Author:    smartwy
#Date:     
#Version:


# from tkinter import *
#
# class Application(Frame):
# 	def __init__(self,master=None): # master，在Tkinter中，一个控件可能属于另一个控件，这时另一个控件就是这个控件的master。默认一个窗口没有master，因此master有None的默认值。
# 		Frame.__init__(self,master) # 调用Application的父类Frame的__init__函数初始化Application类的Frame类部分。
# 		self.pack() # 布局
# 		self.createWidget() # 创建widget
#
# 	def createWidget(self):
# 		self.helloLabel = Label(self,text='hello world !') # 创建标签
# 		self.helloLabel.pack() # 把widget加入到父容器中
# 		self.quitButton = Button(self,text='quit',command=self.quit) # 创建按钮及动作
# 		self.quitButton.pack() # 把widget加入到父容器中
#
# app = Application() # 实例对象
# app.master.title('test GUI') # 设置窗口名称
# app.mainloop() # 主消息循环

from tkinter import  *
import tkinter.messagebox as messagebox

class Application(Frame):
	def __init__(self,master=None):
		Frame.__init__(self,master)
		self.pack()
		self.createWidget()
	def createWidget(self):
		self.inputInput = Entry(self)
		self.inputInput.pack()
		self.enterButton = Button(self,text='Enter',command=self.hello)
		self.exitButton = Button(self,text='quit',command=self.quit)
		self.exitButton.pack()
		self.enterButton.pack()
	def hello(self):
		name = self.inputInput.get() or 'world'
		messagebox.showinfo('message','hello,%s'% name)
		self.exitButton = Button(self,text='exit',command=self.quit)
		self.exitButton.pack() # 预期把退出按钮放在弹出窗口，失败

app = Application()
app.master.title('test input gui')
app.mainloop()


