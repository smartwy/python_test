#!/usr/bin/python3
# -*- coding:utf-8 -*-
#P-Name:    python_test
#F-Name:    __init__.py
#Login:     Administrator   
#Descripton:
#Author:    Smartwy
#Date:      2019/7/1 14:13:26
#Version:


from flask import Flask
'''
	create_app
'''
def app():
	app = Flask(__name__)
	return app

