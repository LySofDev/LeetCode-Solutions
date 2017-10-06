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
	'''
	cs: String -> Original text
	return: String -> Longest, palindromic substring
	'''
	# Set first character index to 0
	x = 0

	# While at least two characters remain in string
	while x < len(cs) - 1:

		# Set last character index to last index in string
		y = len(cs)

		# While at least two characters remain between first and last
		while (len(cs) - x) - (len(cs) - y) > 1:

			# Get substring from characters
			ss = cs[x:y]

			# If substring has more than one character and is palindrome
			if len(ss) > 1 and ss == ss[::-1]:

				# Return current substring
				return ss

			# Increment last character index by 1
			y -= 1

		# Increment first character index by 1
		x += 1


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
