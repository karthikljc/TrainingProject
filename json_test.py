import unittest
import csv_function
import json
import csv

class MyTest(unittest.TestCase):

	def test_parser(self):
		expected_output={"coord":{"lon":-0.13,"lat":51.51}}
		#filename='data.json'
		#actual_output=csv_function.parser(filename ,'data/path')
		actual_output=csv_function.parser(obj)
		self.assertContains(actual_output,expected_output)	
		
	def test_parser1(self):
	
		Expt_output={"clouds":{"all":90}}
		actual_output={"clouds":{"all":90}}
		self.assertDictEqual(Expt_output,actual_output)
		
	def test_parser2(self):
		expected_output={"coord":{"lon":-0.13,"lat":51.51}}
		actual_output={"lon":-0.13,"lat":51.51}
		self.assertDictEqual(expected_output,actual_output)
		
	def test_parser3(self):
		sample_json={"coord":{"lon":-0.13,"lat":51.51}}
		path = 'D:\TrainingProject'
		filename='data.json'
		self.assertIn( csv_function.parser(filename, path) , sample_json)
	
	
	
	
if __name__ == '__main__':
	unittest.main()