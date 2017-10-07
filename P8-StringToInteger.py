'''
8. Strign To Integer

Implement atoi to convert a string to an integer.

Hint: Carefully consider all possible input cases. If you want a challenge, please do not see below and ask yourself what are the possible input cases.

Notes: It is intended for this problem to be specified vaguely (ie, no given input specs). You are responsible to gather all the input requirements up front.
'''
import unittest as ut


def main(cs):
	'''
	cs: String -> Text representing an integer
	return: Integer -> Number represented by text
	'''
	# SOLUTION
	pass
	

class Tests (ut.TestCase):

	def testA(self):
		s = "123"
		expected = 123
		result = main(s)
		self.assertEqual(expected, result)
		
	def testB(self):
		s = "-45"
		expected = -45
		result = main(s)
		self.assertEqual(expected, result)
		
	def testC(self):
		s = "   1000"
		expected = 1000
		result = main(s)
		self.assertEqual(expected, result)
		
	def testD(self):
		s = "152   "
		expected = 152
		result = main(s)
		self.assertEqual(expected, result)
		
	def testE(self):
		s = "fail"
		expected = None
		result = main(s)
		self.assertEqual(expected, result)


if __name__ == '__main__':
	ut.main()
