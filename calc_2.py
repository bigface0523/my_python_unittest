#-*- coding: utf-8 -*-
# http://www.jackman.cn/?p=1009

class calculator(object):
    def add(self, a, b):
        return a + b

    def sub(self, a, b):
        return a - b

    def mul(self, a, b):
        return a*b


import unittest

class TestCalculatorFunctions(unittest.TestCase):

    def setUp(self):
        ''' initialization '''
        print ()
        print ("初始化")
        self.num = calculator()

    def tearDown(self):
        ''' run end ,release '''
        print ("結束")
        self.num = None

    def test_add(self):
        ret = self.num.add(1,2)
        self.assertEqual(ret, 3)

    def test_sub(self):
        ret = self.num.sub(0,1)
        self.assertEqual(ret, -1)

    def test_mul(self):
        ret = self.num.mul(5, 6)
        self.assertEqual(ret, 30)

def suite():
    suite = unittest.TestSuite()
    suite.addTest(TestCalculatorFunctions('test_add'))
    #suite.addTest(TestCalculatorFunctions('test_sub'))
    suite.addTest(TestCalculatorFunctions('test_mul'))
    return suite

if __name__ == '__main__':
    unittest.main(defaultTest = 'suite')
#    unittest.main()