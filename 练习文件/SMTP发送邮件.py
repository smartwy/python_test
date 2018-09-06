# -*- coding:utf-8 -*-
#Name:     
#Descripton: pop3收取邮件没有写，可前去https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/0014320098721191b70a2cf7b5441deb01595edd8147196000 学习
#Author:    smartwy
#Date:     
#Version:

from email.mime.text import MIMEText
msg = MIMEText('Hello ,This is by python test email.', 'plain', 'utf-8')

# from_addr = input('Email user :')
# password = input("Email passwd :")
# to_addr = input('The email to who :')
from_addr = 'wangye1989_0226@163.com'
password = 'wangye13141314'
to_addr = 'wy120649294@163.com'
smtpserver = 'smtp.163.com'
# 下面三行表示 发送地址，接收地址，邮件主题，不谢报554 DT.SPM错误
msg['from'] = from_addr
msg['to'] = to_addr
msg['subject'] = 'test email'

import smtplib
server = smtplib.SMTP(smtpserver, 25)
server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()



