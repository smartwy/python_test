#!/usr/bin/python3
# -*- coding:utf-8 -*-
#Name:     
#Descripton:
#Author:    smartwy
#Date:     
#Version:

import numpy as np
import pandas as pd

# datal = [i for i in ['a1','a2','a3','a4','a5']]
# data_s = pd.Series(datal, index=list('abcde'))
# print(data_s,data_s.index,data_s.values,'**********', sep='\n')
# print(data_s['b':'e'])
# print(data_s[[1,2,3]],'**********', sep='\n')
# print(data_s.items)


datal = ['4','13', '12','15']
datadt = ['14','26', '25','35']
# numpy.array(object, dtype = None, copy = True, order = None, subok = False, ndmin = 0)
a = np.array([datal,datadt],dtype=int, ndmin=2)
print(a)