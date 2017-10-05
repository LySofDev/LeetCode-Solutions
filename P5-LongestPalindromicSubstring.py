'''
5. Longest Palindromic Substring

Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example:

Input: "babad"

Output: "bab"

Note: "aba" is also a valid answer.

Example:

Input: "cbbd"

Output: "bb"
'''
import unittest as ut


def main(cs):
	# SOLUTION
	pass


class Tests (ut.TestCase):

	def testA(self):
		string = "babad"
		expected = "bab"
		result = main(string)
		self.assertEqual(expected, result)

	def testB(self):
		string = "cbbd"
		expected = "bb"
		result = main(string)
		self.assertEqual(expected, result)


if __name__ == '__main__':
	ut.main()
