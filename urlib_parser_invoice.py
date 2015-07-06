import urllib.request
import unittest
from html.parser import HTMLParser

class Parser_Invoice(HTMLParser):
	def __init__(self):
		HTMLParser.__init__(self)
		self.isNumber = 0
		self.numbers = []

	def handle_data(self, data):
		if self.isNumber == 1:
			#print(data)
			self.numbers.append(data)
			self.isNumber = 0

	def handle_starttag(self, tag, attrs):
		if tag == 'span' and attrs == [('class','t18Red')]:
			self.isNumber = 1

	def get_ans(self):
		return self.numbers

class Test_Parser_Invoice(unittest.TestCase):
	def setUp(self):
		data = urllib.request.urlopen('http://invoice.etax.nat.gov.tw')
		content = data.read().decode('utf_8')
		data.close()
		
		self.Par = Parser_Invoice()
		bingo = self.Par.feed(content)

	def test_input(self):
		print ("")
		print (self.Par.get_ans())
		self.assertEqual(self.Par.get_ans()[0], str(46492032))
		#self.assertEqual(self.Par.get_ans()[1], str(66224881))
		#self.assertEqual(self.Par.get_ans()[2], str(1145))

	def test_input_2(self):
		self.assertEqual(self.Par.get_ans()[1], str(66224881))
	def tearDown(self):
		pass

if __name__ == '__main__':
    unittest.main()


'''
['46492032', '66224881', '06216938、04296940、86442491', '306、403、867', '60538
935', '50887710', '63856949、39459262、61944942', '022、355、038']
..
