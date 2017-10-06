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
	# Initiate the result to 0
	r = 0
	
	# Check if input is negative
	n = x < 0
	
	# If input is negative
	if n:
		
		# Set input to positive
		x = -x
	
	# While original integer is not 0
	while x:
		
		# Extract last digit
		d = x % 10
		
		# Remove last digit
		x = x // 10
	
		# Increase result by 10
		r *= 10
		
		# Append last digit to result
		r += d
		
	# If input was negative
	if n:
		
		# Set result to negative
		r = -r
		
	# Return the result
	return r


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
