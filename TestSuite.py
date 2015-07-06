#-*- encoding: UTF-8 -*-
# https://github.com/akun/pm/blob/master/docs/unittest/example_test_suite.py
import unittest
class ExampleTestCase(unittest.TestCase):

    def test_do_somthing(self):
        self.assertEqual(1, 1)

    def test_do_somthing_else(self):
        self.assertEqual(1, 1)
        
class AnoterExampleTestCase(unittest.TestCase):

    def test_do_somthing(self):
        self.assertEqual(1, 1)

    def test_do_somthing_else(self):
        self.assertEqual(1, 1)

def suite_use_make_suite():
    """想把TestCase下的"所有"测试加到TestSuite的时候可以这样用"""

    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(ExampleTestCase))
    #suite.addTest(unittest.makeSuite(AnoterExampleTestCase))
    return suite

def suite_add_one_test():
    """想把TestCase下的"某个"测试加到TestSuite的时候可以这样用"""

    suite = unittest.TestSuite()
    suite.addTest(ExampleTestCase('test_do_somthing'))
    return suite

def suite_use_test_loader():
    """想用"TestLoader"方式把测试加到TestSuite的时候可以这样用"""

    test_cases = (ExampleTestCase, AnoterExampleTestCase)
    suite = unittest.TestSuite()
    for test_case in test_cases:
        tests = unittest.defaultTestLoader.loadTestsFromTestCase(test_case)
        suite.addTests(tests)
    return suite

if __name__ == '__main__':

    # 使用 TestLoader 方法把 test 放到 TestSuite 來測試
    #unittest.main(defaultTest='suite_use_test_loader')

    #使用 TestSuite 方法測試某個 test
    #unittest.main(defaultTest='suite_add_one_test')

    #將 TestCase 中所有 test 放到 TestSuite 來測試
    unittest.main(defaultTest='suite_use_make_suite')
