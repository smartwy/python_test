#!/usr/bin/python3
# -*- coding:utf-8 -*-
#P-Name:    python_test
#F-Name:    manage.py
#Login:     Administrator   
#Descripton:
#Author:    Smartwy
#Date:      2019/7/1 14:13:12
#Version:

# blueprint : 蓝图， 视图模块化


from flask import Flask, render_template
# from .blue_print import create_app
from admin import ad # 导入蓝图模块
from user import us

app = Flask(__name__)
# app.config['SERVER_NAME'] = ''

@app.route('/')
def hello():
	return render_template('hello.html')

#这里分别给app注册了两个蓝图ad,us
#参数url_prefix='/xxx'的意思是设置request.url中的url前缀，
#即当request.url是以/admin或者/user的情况下才会通过注册的蓝图的视图方法处理请求并返回

app.register_blueprint(ad,url_prefix='/admin') # 注册蓝图模块
app.register_blueprint(us, url_prefix='/user')


if __name__ == '__main__':
	app.run(debug=True)


