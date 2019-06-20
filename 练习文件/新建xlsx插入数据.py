#!/usr/bin/python3
# -*- coding:utf-8 -*-
#Name:     
#Descripton:
#Author:    smartwy
#Date:     
#Version:

# 新建xlsx文件，插入数据，不能对已存在的文件进行编辑
import xlsxwriter

swr = xlsxwriter.Workbook('E:\\python_project_dir\\python_test\\练习文件\\testxlsx.xlsx') # 创建文件
sheet = swr.add_worksheet(name='表单') # 添加表单名称
sheet.write_row('A1',data=['序号','名字','电话']) # 在A1处横向插入三条数据
sheet.write_row('A2',data=['1','佩奇','188888'])# 在A2处横向插入三条数据
bold = swr.add_format({'bold': 5,'color':'red', 'italic':True}) # 红字，加粗，斜体
sheet.write_row('A3',data=['上面是row插入，下面是column插入'],cell_format=bold)
sheet.write_column('A4',data=['序号', '名字', '电话'])
sheet.write_column('B5',data=['2', '乔治', '188989'])
swr.close() # 关闭

# 下方链接为模块官方说明
# https://xlsxwriter.readthedocs.io/chart.html
