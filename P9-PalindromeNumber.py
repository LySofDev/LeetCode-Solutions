'''
9. Palindrome Number

Determine whether an integer is a palindrome. Do this without extra space.

click to show spoilers.

Some hints:
Could negative integers be palindromes? (ie, -1)

If you are thinking of converting the integer to string, note the restriction of using extra space.

You could also try reversing an integer. However, if you have solved the problem "Reverse Integer", you know that the reversed integer might overflow. How would you handle such case?

There is a more generic way of solving this problem.
'''
import unittest as ut


def main(n):
	'''
	n: Integer -> Number to verify
	return: Boolean -> True if palindrome, False otherwise
	'''
	# Return false if number is negative
	if n < 0:
		return False

	# Copy original number
	c = n

	# Initiate reversed number to 0
	r = 0

	# While copy of number still has digits
	while c:

		# Append last digit to reversed number
		r = (r * 10) + (c % 10)

		# Remove last digit from copy of number
		c = c // 10

	# Return true if reversed number is equal to original number
	return n == r


class Tests (ut.TestCase):

	def testA(self):
		n = 454
		expected = True
		result = main(n)
		self.assertEqual(expected, result)

	def testB(self):
		n = 934
		expected = False
		result = main(n)
		self.assertEqual(expected, result)

	def testC(self):
		n = 1001
		expected = True
		result = main(n)
		self.assertEqual(expected, result)

	def testD(self):
		n = 5
		expected = True
		result = main(n)
		self.assertEqual(expected, result)

	def testE(self):
		n = 9128
		expected = False
		result = main(n)
		self.assertEqual(expected, result)

	def testF(self):
		n = 0
		expected = True
		result = main(n)
		self.assertEqual(expected, result)

	def testG(self):
		n = -676
		expected = False
		result = main(n)
		self.assertEqual(expected, result)


if __name__ == '__main__':
	ut.main()
