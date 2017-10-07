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
	r = 0
	n = False
	s = False
	f = False
	
	for c in cs:
		
		if c == '-':
			
			if s:
				
				return 0
				
			else:
				
				s = True
				
				n = True
				
		elif c.isnumeric():
			
			if not s:
				
				s = True
				
			if f:
				
				return 0
			
			r = r * 10 + int(c)
			
		elif c == ' ' and s:
			
			f = True
			
		elif c != ' ':
			
			return 0
			
	if n:
		
		r = -r
			
	return r
			

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
		expected = 0
		result = main(s)
		self.assertEqual(expected, result)
		
	def testF(self):
		s = "-45-3"
		expected = 0
		result = main(s)
		self.assertEqual(expected, result)
		
	def testG(self):
		s = "34 8"
		expected = 0
		result = main(s)
		self.assertEqual(expected, result)


if __name__ == '__main__':
	ut.main()
