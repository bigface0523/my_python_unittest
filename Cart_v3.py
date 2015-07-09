#-*- coding : utf-8 -*-
import unittest
import time
class Item():
	def __init__(self, item_name, price, class_name):
		self.name = item_name
		self.price = price
		self.class_name = class_name

	def setName(self, name):
		self.name = name

	def setPrice(self, price):
		self.price = price

	def getName(self):
		return self.name

	def getPrice(self):
		return self.price

class Foods(Item):
	pass

class Daily_use(Item):
	pass

class Alcohol(Item):
	pass

class Electron(Item):
	pass
		
###############  購物車  ###############################

class Cart():
	def __init__(self):
		#self.list = []
		self.today = time.strftime('%Y.%m.%d', time.localtime(time.time()))
		self.today_promotion = []	#discount, item_class
		
		#item, quantity
	def add(self, *shopping_list):
		itr = iter(shopping_list)
		money = 0	
		ans = ""
		for i in range(int(len(shopping_list)/2)):
			item = next(itr)
			quantity = next(itr)
			
			ans += str(quantity) + "*" + item.getName() + ":" + str(item.getPrice()) + "\n"
			#self.list.append(item)
			#self.list.append(quantity)
			money += item.getPrice() * quantity * self.get_discount(item.class_name)

		if len(self.today_promotion) == 0:
			print()
		else:
			for i, j in enumerate(self.today_promotion):
				if i % 2 == 0:
					print (self.today+"|"+str(self.today_promotion[i])+"|"+self.today_promotion[i+1])

		print (ans)
		print (money)
		return money


	def check_promotion(self, *promotion_info):
		item_class_list = ["Foods", "Daily_use", "Electron", "Alcohol"]
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
			if item_class_tmp not in item_class_list:
				return "促銷品類有誤"

			self.today_promotion.append(discount_tmp)
			self.today_promotion.append(item_class_tmp)
		return "促銷測試通過"

		# today_promotion : discount, item_class
	def get_discount(self, item_class):
		for i, j in enumerate(self.today_promotion):
			if j == item_class:
				return self.today_promotion[i-1]
		return 1

class Test_Cart(unittest.TestCase):


	def setUp(self):

		self.snack = Foods("餅乾", 40, "Foods")
		self.bread = Foods("麵包", 25, "Foods")
		self.cake = Foods("蛋糕", 65, "Foods")
		self.beef = Foods("牛肉", 125, "Foods")
		self.fish = Foods("魚", 90, "Foods")
		self.vegetable = Foods("蔬菜", 35, "Foods")

		self.tossil = Daily_use("餐巾紙", 40, "Daily_use")
		self.box = Daily_use("收納箱", 300, "Daily_use")
		self.cup = Daily_use("咖啡杯", 280, "Daily_use")
		self.umbrella = Daily_use("雨傘", 499, "Daily_use")

		self.beer = Alcohol("啤酒", 75, "Alcohol")
		self.white_wine = Alcohol("白酒", 450, "Alcohol")
		self.vodka = Alcohol("伏特加", 300, "Alcohol")

		self.iPad = Electron("iPad", 7999, "Electron")
		self.iPhone = Electron("iPhone", 23000, "Electron")
		self.monitor = Electron("螢幕", 3500, "Electron")
		self.laptop = Electron("筆記型電腦", 32000, "Electron")
		self.keyboard = Electron("鍵盤", 599, "Electron")


		print ()
		print ("----------------")
		print ("測試開始 setUp")
		print ("----------------")
		self.my_cart = Cart()
		pass

	def tearDown(self):
		pass

	def test_1(self):
		print("test_1")
		self.assertEqual(self.my_cart.check_promotion("2015.07.09", 0.1, "Foods", "2015.07.09", 0.9, "Daily_use"), "促銷測試通過")
		self.assertEqual( self.my_cart.add(self.snack, 3, self.bread, 7, self.umbrella, 1),  478.6)

	def test_2(self):
		self.assertEqual(self.my_cart.check_promotion("2015.07.09", 0.9, "Electron"), "促銷測試通過")
		self.assertEqual( self.my_cart.add(self.snack, 3), 120 )	

	def test_3(self):
		self.assertEqual( self.my_cart.add(self.cup, -9), 2520 )	

	def test_4(self):
		self.assertEqual( self.my_cart.add(self.beef, 9), 1125 )	

	def test_5(self):
		self.assertEqual(self.my_cart.check_promotion("1999.07.09", 0.9, "Foods"), "促銷測試通過")
		self.assertEqual( self.my_cart.add(self.tossil, 2, self.snack, 1), 116 )		

	def test_6(self):
		self.assertEqual(self.my_cart.check_promotion("2015.07.09", 0.5, "Daily_use"), "促銷測試通過")
		self.assertEqual( self.my_cart.add(self.box, 10, self.snack, 1), 1540 )			

	def test_7(self):
		self.assertEqual(self.my_cart.check_promotion("2015.07.09", 0.85, "Electron", "2015.07.09", 0.7, "Alcohol"), "促銷測試通過")
		self.assertEqual( self.my_cart.add(self.laptop, 1, self.beer, 24), 28460 )				

if __name__=="__main__":
	unittest.main()
