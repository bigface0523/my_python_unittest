#!/usr/bin/python
#-*- coding : utf-8 -*-
import unittest
		# assertTrue
		# assertFalse
		# assertEqual
		# assertNotEqual
		#self.assertEqual(self.p.getName(), "Andy")
class Person:
	def __init__(self, name):
		print ("init")
		self.name = name
		self.age = 10
	def getName(self):
		return self.name
	def setAge(self, age):
		self.age = age


class TestPerson(unittest.TestCase):
	def setUp(self):
		print ()
		print (u"初始化 setUp")
		self.p = Person("Andy")

	def test_getName(self):
		print (u"測試 test_getName :")
		self.assertNotEqual(self.p.getName(), "Car")

	def test_setAge(self):
		print (u"測試 test_setAge :")
		self.assertEqual(self.p.age, 10)
		self.p.setAge(18)
		#self.assertNotEqual(self.p.age, 18)	

	def tearDown(self):
		print (u"結束測試 tearDown")

if __name__=="__main__":
	unittest.main()