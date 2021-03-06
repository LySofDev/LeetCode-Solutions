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
	'''
	x: Integer -> Original number
	return: Integer -> Original number reversed
	'''
	# Set copy of input to input
	c = x
	
	# Initiate the result to 0
	r = 0
	
	# Set copy to positive if input is negative
	if x < 0:
		c = -c
	
	# While original integer is not 0
	while c:
		
		# Append last digit to result
		r = r * 10 + c % 10
		
		# Remove last digit
		c = c // 10
		
	# Set result to negative if input is negative
	if x < 0:
		r = -r
		
	# Return the result
	return r
	

def copy(x):
	'''
	x: Integer -> Original value
	return: Integer -> Copy of original value
	'''
	return x
	
def zero():
	'''
	return: Integer -> Literal zero
	'''
	return 0
	
def is_negative(x):
	'''
	x: Integer -> Number
	return: Boolean -> True if negative, False otherwise
	'''
	return x < 0
	
def negate(x):
	'''
	x: Integer -> Number
	return: Integer -> Negated number
	'''
	return -x
	
def not_zero(x):
	'''
	x: Integer -> Number
	return: Boolean -> False if number is 0, True otherwise
	'''
	return x != 0
	
def get_last_digit(x):
	'''
	x: Integer -> Number
	return: Integer -> Last digit of number
	'''
	return x % 10
	
def remove_last_digit(x):
	'''
	x: Integer -> Number
	return: Integer -> Number without last digit
	'''
	return x // 10
	
def append_digit(r, d):
	'''
	r: Integer -> Resulting number
	d: Integer -> Digit to append
	'''
	return r * 10 + d
	
	
def verboseMain(original):
	'''
	original: Integer -> Original number
	return: Integer -> Original number reversed
	'''
	number = copy(original)
	result = zero()
	
	if is_negative(original):
		number = negate(number)
		
	while not_zero(number):
		digit = get_last_digit(number)
		number = remove_last_digit(number)
		result = append_digit(result, digit)
		
	if is_negative(original):
		result = negate(result)
		
	return result
	

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
		
	def testC(self):
		x = 123
		expected = 321
		result = verboseMain(x)
		self.assertEqual(expected, result)
	
	def testD(self):
		x = -123
		expected = -321
		result = verboseMain(x)
		self.assertEqual(expected, result)
		
		

if __name__ == '__main__':
	ut.main()
