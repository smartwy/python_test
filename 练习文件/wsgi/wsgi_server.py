# -*- coding:utf-8 -*-
#Name:     
#Descripton:
#Author:    smartwy
#Date:     
#Version:


from wsgiref.simple_server import make_server
from wsgi_hello import application

httpd = make_server('',8000,application)
print('start wsgi ok ')
httpd.serve_forever()


