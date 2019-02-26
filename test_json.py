import unittest
import csv
import json
import csv_function

class MyTest(unittest.TestCase):
	
	def test_parser(self):
		data={"coord":{"lon":-0.13,"lat":51.51}
		self.assertEqual(csv_function.parser(obj), data)
		
	def test_parser1(self):
		data1="weather":[{"id":300,"main":"Drizzle","description":"light intensity drizzle","icon":"09d"}]
		path=d:\TrainingProject
		filename=data.json
		self.assertEqual(parser(path,filename), data)
		
	def test_parse2(self):
		result=csv_function.parser(obj)
		icon="09d"
		self.assertEqual(result , icon)
	def test_parser3(self):
		result2="clouds":{"all":90}	
		self.assertEqual(csv_function.parser(self.(data.json)[6]), result2)
	
if __name__ == '__main__':
	unittest.main()