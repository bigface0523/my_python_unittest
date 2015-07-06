import unittest
import urllib.request

class Test_WebStatus(unittest.TestCase):

	@unittest.expectedFailure
	def test_404(self):
		respone = urllib.request.urlopen('http://localhost:5000/todo/api/v1.0/tasks/3')
		print ("結果 : " + str(respone.getcode()))
		self.assertTrue(respone.getcode() == 404)

	def test_200(self):
		respone = urllib.request.urlopen('http://localhost:5000/todo/api/v1.0/tasks/1')
		print ("結果 : " + str(respone.getcode()))
		self.assertTrue(respone.getcode() == 200)

def use_test_suite():
	suite = unittest.TestSuite()
	suite.addTest(unittest.makeSuite(Test_WebStatus))
	return suite

if __name__=="__main__":
	unittest.main(defaultTest = 'use_test_suite')
