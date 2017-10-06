'''
7. Reverse Integer

Reverse digits of an integer.

Example1: x = 123, return 321
Example2: x = -123, return -321

click to show spoilers.

Note:
The input is assumed to be a 32-bit signed integer. Your function should
return 0 when the reversed integer overflows.
'''
import unittest as ut


def main(x):
	# SOLUTION
	pass
	

class Tests (ut.TestCase):

	def testA(self):
		x = 123
		expected = 321
		result = main(x)
		self.assertEqual(expected, result)
	
	def testB(self):
		x = -123
		expected = -321
		result = main(x)
		self.assertEqual(expected, result)
		

if __name__ == '__main__':
	ut.main()
