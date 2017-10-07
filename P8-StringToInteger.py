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
	# Set resulting integer to 0
	r = 0
	
	# Set negative? to False
	n = False
	
	# Set started? to False
	s = False
	
	# Set finished? to False
	f = False
	
	# Iterate over each character in given string
	for c in cs:
		
		# If character is negative symbol
		if c == '-':
			
			# If started?
			if s:
				
				# Error has ocurred during conversion
				return 0
				
			# If not started?
			else:
				
				# Set started? to True
				s = True
				
				# Set negative? to True
				n = True
				
		# If character is numeric
		elif c.isnumeric():
			
			# If not started?
			if not s:
				
				# Set started? to True
				s = True
				
			# If finished?
			if f:
				
				# Error has ocurred during conversion
				return 0
			
			# Convert character to int and append to resulting integer
			r = r * 10 + int(c)
			
		# If character is whitespace and started?
		elif c == ' ' and s:
			
			# Set finished? to True
			f = True
			
		# If character is not whitespace
		elif c != ' ':
			
			# Error has ocurred during conversion
			return 0
			
	# If negative?
	if n:
		
		# Negate resulting integer
		r = -r
			
	# Return resulting integer
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
