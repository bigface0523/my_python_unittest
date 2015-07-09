#-*- coding : utf-8 -*-
import unittest
import time
import datetime

class Cart:

	def __init__(self):
		self.today = time.strftime('%Y.%m.%d', time.localtime(time.time()))
		self.today_promotion = []	#discount, item_class
		self.食品 = {
			"麵包" 	: 25,
			"餅乾" 	: 35,
			"蛋糕"	: 70,
			"牛肉"	: 130,
			"魚"	: 90,
			"蔬菜" 	: 50
		}

		self.酒類 = {
			"啤酒" : 70,
			"白酒" : 120,
			"伏特加" : 80
		}

		self.電子 = {
			"iPad" : 7999,
			"iPhone" : 23000,
			"螢幕" :3299,
			"筆記型電腦" : 28900,
			"鍵盤" : 350,
		}

		self.日用品 = {
			"餐巾紙" : 35,
			"收納箱" : 220,
			"咖啡杯" : 350,
			"雨傘" : 499
		}

		self.item_list = {
			"食品" : self.食品,
			"酒類" : self.酒類,
			"電子" : self.電子,
			"日用品" : self.日用品
		}

	def sum(self, *item):		
		money = 0
		ans = ""
		itr = iter (item)
		for i in range(int(len(item)/2)):
			quantity = next(itr) 
			item_name = next(itr)			
			price = self.check_item_in_list(item_name)
			if price == "商品不存在":
				return "商品不存在"
		
			money += price * quantity
			ans += str(quantity) + " * " + item_name + " : " + str(price) + "\n"

		ans += "\n總金額 = " + str(money) + "\n\n" + self.today

		if len(self.today_promotion) == 0:
			print()
		else:
			for i, j in enumerate(self.today_promotion):
				if i % 2 == 0:
					print (self.today+"|"+str(self.today_promotion[i])+"|"+self.today_promotion[i+1])

		print ()		
		print (ans)	
		return money

		# 清單有沒有此 item, 回傳值為此 item 的金額
	def check_item_in_list(self, item_name):
		for i in self.item_list:
			for j in self.item_list[i]:
				if item_name in self.item_list[i]:
					return self.item_list[i][item_name] * self.get_discount(i)
		return "商品不存在"

		# date, discount, item_class
	def check_promotion(self, *promotion_info):
		itr = iter(promotion_info)
		discount_tmp = 0
		item_class_tmp = ""

		for i in range(int(len(promotion_info)/3)):
			if next(itr) != self.today:
				return "促銷日期有誤"

			discount_tmp = next(itr)
			if discount_tmp <=0 or discount_tmp >=1:
				return "促銷折扣有誤"

			item_class_tmp = next(itr)
			if item_class_tmp not in self.item_list:
				return "促銷品類有誤"

			self.today_promotion.append(discount_tmp)
			self.today_promotion.append(item_class_tmp)
		return "促銷測試通過"

	def get_discount(self, item_class):
		for i, j in enumerate(self.today_promotion):
			if j == item_class:
				return self.today_promotion[i-1]
		return 1
	
class Test_Cart(unittest.TestCase):
	def setUp(self):
		print ()
		print ("----------------")
		print ("測試開始 setUp")
		print ("----------------")
		self.my_cart = Cart()
		pass

	def tearDown(self):
		pass

	def test_1(self):
		self.assertEqual(self.my_cart.check_promotion("2015.07.09", 0.1, "電子", "2015.07.09", 0.9, "日用品", "2015.07.09", 0.95, "酒類"), "促銷測試通過")
		self.assertEqual(self.my_cart.sum(3, "麵包", 5, "餅乾", 3, "白酒", 1, "筆記型電腦", 6, "牛肉"), 4262)

	def test_2(self):
		self.assertEqual(self.my_cart.check_promotion("2015.07.100", 0.9, "酒類"), "促銷測試通過")
		self.assertEqual(self.my_cart.sum(3, "啤酒", 1, "餐巾紙"), 224)

	def test_3(self):
		self.assertEqual(self.my_cart.sum(3, "啤酒"), 210)

def testSuite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(Test_Cart))
    return suite

if __name__=="__main__":
	unittest.main(defaultTest='testSuite')
