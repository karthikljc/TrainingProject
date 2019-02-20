import unittest
import addsub

class TestCalc(unittest.TestCase):
	def test_add(self):
		result=addsub.add(10, 5)
		self.assertEqual(result, 15)
	def test_subtract(self):
		result=addsub.subtract(15, 300)
		self.assertEqual(result, 5)
	def test_multiply(self):
		result=addsub.multiply(2, 3)
		self.assertEqual(result, 6)

if __name__ == '__main__': 
    unittest.main()		
