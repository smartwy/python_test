# -*- coding:utf-8 -*-
#Name:     
#Descripton:
#Author:    smartwy
#Date:     
#Version:

import re

m = re.search('(?<=abc)def','abcdefiijijiiabcdef')
print(m.group(0))



