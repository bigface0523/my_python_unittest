import unittest
class Get_Next(object):
	def __init__(self, array):
		self.my_list = array
		print (self.my_list)

	def getNext(self, x):
		iterator = iter(self.my_list)
		for elem in self.my_list:
			next (iterator)
			if elem ==  x:
				return (next (iterator))
		return -1
			
class Test_Get_Next(unittest.TestCase):
	def setUp(self):
		print ("setUp")
		self.li = Get_Next([1,2,3,4,5,6,7,2,2])

	def test_getNext(self):
		print ("test_getNext")
		self.assertEqual(self.li.getNext(1), 3)

	def tearDown(self):
		print ("tearDown")
		
if __name__ == '__main__':
	unittest.main()