import unittest
import calc
class TestCalC(unittest.Testcase):

	def test_add(self):
		result=calc.add(10,5)
		self.assertEqual(result,15)