# -*- coding:utf-8 -*-
#Name:     
#Descripton:
#Author:    smartwy
#Date:     
#Version:

from flask import request,Flask,render_template

app = Flask(__name__)
@app.route('/',methods=['GET','POST'])
def home():
	return render_template('home.html')

@app.route('/login',methods=['GET'])
def login_form():
	return render_template('form.html')

@app.route('/login',methods=['POST'])
def login():
	username = request.form['username']
	password = request.form['password']
	if username == 'admin' and password == '123456':
		return render_template('login_ok.html', username=username)
	return render_template('form.html', message='Bad username or password', username=username)

if __name__ == '__main__':
	app.run()


