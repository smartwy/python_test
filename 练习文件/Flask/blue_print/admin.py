#!/usr/bin/python3
# -*- coding:utf-8 -*-
#P-Name:    python_test
#F-Name:    admin.py
#Login:     Administrator   
#Descripton:
#Author:    Smartwy
#Date:      2019/7/1 14:30:06
#Version:

from flask import Blueprint,render_template,redirect,request,abort

ad = Blueprint('ad', __name__)

@ad.route('/login')
def login():
	return render_template("adlogin.html")

@ad.route('/login_ing',methods=['POST'])
def login_i():
	u = request.form['username']
	p = request.form['password']
	if u == 'admin' and p == '123456':
		return render_template("loginok.html",u=u)
	return render_template("adlogin.html")

@ad.route('/wy')
def wy():
	return redirect('/admin/login')

@ad.route('/er')
def erf():
	abort(404)

@ad.errorhandler(404)
def erm(er):
	return 'this is 404 page !'
