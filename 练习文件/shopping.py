# -*- coding:utf-8 -*-
#Name:      shopping car
#Descripton:
#Author:    smartwy
#Date:      2018-4-10
#Version:

goods = [{"name": "电脑", "price": 1999},{"name": "鼠标", "price": 10},
         {"name": "游艇", "price": 20},{"name": "美女", "price": 998},]
i = 0
flg = 0
l = []
money = 0
money_old = 0
for x in goods:
	l.append(goods[i]["price"])
	i += 1
else:
	#l_min = sorted(l)[0]
	l_min = min(l)
while flg < 3:
	if money is 0:
		money = int(input("请输入您的金额："))
	if money < l_min :
		print("您的金额不足！")
		flg = 2
	else:
		for x,go in enumerate(goods,1):
			print(x,go["name"],"¥:",go["price"])
		ara,araNum = input("输入您要够买的商品编号与数量：").split()
		ara = int(ara)
		araNum = int(araNum)
		if ara > 4:
			print("超出现有商品编号！")
		else:
			#print(goods[ara-1]["price"])
			money_old = money
			araNum_sum = goods[ara - 1]["price"] * araNum
			money = money - araNum_sum
			if money < 0:
				print("余额为%d ，不足以够买您选中的商品！"% money_old)
				flg = 2
			else:
				print("您购买了%s个%s ! 花费了%d! 余额为%d! "%(araNum,goods[ara-1]["name"],araNum_sum,money))
				inp = input("是否继续够买商品?(y/n):")
				if inp is "N" or inp is "n" or inp is "no" or money is 0:
					flg =4

	flg += 1
	if flg is 3:
		arg = input("是否继续？（Y/N）:")
		if arg is "Y" or arg is "y" or arg is "yes":
			flg = 0
			print("继续交易！")
			money = money_old
		else:
			flg = 4
			print("终止交易！")

