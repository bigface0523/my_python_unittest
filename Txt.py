import unittest
import os
class MyFile(object):
	def __init__(self, fileName):
		print ("MyFile init")
		self.fileName = fileName

	def write_txt(self, txt):
		print ("MyFile write txt")
		self.file = open(self.fileName, 'w')
		self.file.write(txt)
		self.file.close()

	def read_txt(self):
		print ("MyFile read txt")
		self.file = open(self.fileName, 'r')
		self.content = self.file.read()
		self.file.close()
		return self.content

class Test_MyFile(unittest.TestCase):
	def setUp(self):
		print ("測試初始化 setUp")
		self.f = MyFile("Txt_test.txt")

	def get_file_txt(self):
		txt2write = "HELLO"
		print ("測試字串 : " + txt2write)
		return txt2write

	def test_1_write(self):
		print ("寫入測試，檔案是否存在")
		self.f.write_txt(self.get_file_txt())
		self.assertTrue(os.path.isfile(self.f.fileName))

	@unittest.expectedFailure
	def test_2_read(self):
		print ("讀取測試，檔案內容驗證")
		self.content = self.f.read_txt()
		#self.assertEqual(self.get_file_txt(), self.content) 這正確的
		self.assertEqual(self.get_file_txt(), "HELLO PYTHON")

	def tearDown(self):
		pass

if __name__=="__main__":
	unittest.main()