#!/usr/bin/python3
# -*- coding:utf-8 -*-
#Name:     
#Descripton:
#Author:    smartwy
#Date:     
#Version:

# 逻辑有问题，不需opencsdn

import requests
import urllib.request
import codecs
import re
proxy = {'http':'218.18.232.26:80','https':'218.18.232.26:80'}
csdn_url = "http://blog.csdn.net/wangye1989_0226"
blog_url = ["http://blog.csdn.net/wangye1989_0226/article/details/72879403",
            "http://blog.csdn.net/wangye1989_0226/article/details/72896263",
            "http://blog.csdn.net/wangye1989_0226/article/details/72857371",
            ]

class CSDN(object):
    def __init__(self):
        self.csdn_url = csdn_url
        self.blog_url = blog_url
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.96 Safari/537.36', }

    def openCsdn(self):
        req = urllib.request.Request(self.csdn_url, headers=self.headers)
        # req = urllib.request.ProxyHandler(proxy)
        # opener = urllib.request.build_opener(req)
        # data = opener.open("http://blog.csdn.net/wangye1989_0226/article/details/72857371")
        # result = data.read().decode()
        # data.close()
        response = urllib.request.urlopen(req)
        thePage = response.read()
        response.close()
        pattern = '<span class="read-count">阅读数：(\d+)</span>'
        number = ''.join(re.findall(pattern, thePage.decode('utf-8')))
        print(number)

    def openBlog(self):
        for i in range(len(self.blog_url)):
            req = urllib.request.Request(self.blog_url[i])
            response = urllib.request.urlopen(req)
            blog_data = response.read()
            # print(blog_data.decode('utf-8'))
            pattern = '<span class="read-count">阅读数：(\d+)</span>'
            number = ''.join(re.findall(pattern, blog_data.decode('utf-8')))
            print(number)
            response.close()


for i in range(1):
    csdn = CSDN()
    # csdn.openCsdn()
    csdn.openBlog()
    # csdn.openCsdn()

