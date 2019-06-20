# -*- coding:utf-8 -*-
#Name:     
#Descripton:
#Author:    smartwy
#Date:     
#Version:


from flask import Flask
from flask import request

app = Flask(__name__)
@app.route('/',methods=['GET','POST'])
def home():
	return '<h1>home page</h1>'

@app.route('/signin',methods=['GET'])
def signin_form():
	# print(arg)
	return '''<form action="/signin" method="post">
			<p><lable>name : </lable><input name="username"></p>
			<p><lable>pawd : </lable><input name="password" type="password"></p>
			<p><button type="submit">Sign In</button></p>
			</form>'''

@app.route('/signin', methods=['POST'])
def signin():
	# 需要从request对象读取表单内容：
	username = request.form['username']
	password = request.form['password']
	if username=='admin' and password=='password':
		return '<h2>hello admin</h2>'
	return '<h3>Bad username or password</h3>'

if __name__ == '__main__':
	app.run()
