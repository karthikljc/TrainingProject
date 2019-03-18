import unittest
import cubetriangle

class CubeTest(unittest.TestCase):
	def test_cube(self):
		k=cubetriangle.cube(5)
		self.assertEqual(k, 125)
	def test_triangle(self):
		k=cubetriangle.triangle(6, 3)
		self.assertEqual(k, 9)
		
if __name__ == '__main__':
	unittest.main()
	