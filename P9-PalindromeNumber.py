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


def main():
	'''
	return: None
	'''
	# SOLUTION
	pass


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


if __name__ == '__main__':
	ut.main()
