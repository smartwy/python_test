#!/usr/bin/python3
# -*- coding:utf-8 -*-
#P-Name:    python_test
#F-Name:    user.py
#Login:     Administrator   
#Descripton:
#Author:    Smartwy
#Date:      2019/7/1 14:30:15
#Version:


from flask import Blueprint,render_template,redirect

us = Blueprint('us', __name__, template_folder='templates', static_folder='static')

@us.route('/login')
def login():
	return render_template("userlogin.html")

@us.route('/wy')
def wy():
	return redirect('/user/login')



