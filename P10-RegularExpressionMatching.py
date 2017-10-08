'''
10. Regular Expression Matching

Implement regular expression matching with support for '.' and '*'.

'.' Matches any single character.
'*' Matches zero or more of the preceding element.

The matching should cover the entire input string (not partial).

The function prototype should be:
bool isMatch(const char *s, const char *p)

Some examples:
isMatch("aa","a") → false
isMatch("aa","aa") → true
isMatch("aaa","aa") → false
isMatch("aa", "a*") → true
isMatch("aa", ".*") → true
isMatch("ab", ".*") → true
isMatch("aab", "c*a*b") → true
'''
import unittest as ut


def main(cs, r):
	'''
	cs: String -> Original text
	r: String -> Regular expression to match
	return: Boolean -> True if regular expression is matched in Original text
	'''
	# Set regex index to 0
	ri = 0

	# While original text still has characters and regex index is in range
	while len(cs) and len(r) > ri:

		# If first character in original text match current regex character
		if cs[0] == r[ri]:

			# Remove first character from original text
			cs = cs[1:]

			# Increment regex index by 1
			ri += 1

		# If first character in original text doesn't match current regex
		# character
		else:

			return False

	# If regex index is length of regex and original text is empty
	return len(r) <= ri and not len(cs)



class Tests (ut.TestCase):

	def testA(self):
		string = "aa"
		regex = "a"
		expected = False
		result = main(string, regex)
		self.assertEqual(expected, result)

	def testB(self):
		string = "aa"
		regex = "aa"
		expected = True
		result = main(string, regex)
		self.assertEqual(expected, result)

	def testC(self):
		string = "aaa"
		regex = "aa"
		expected = False
		result = main(string, regex)
		self.assertEqual(expected, result)

	def testD(self):
		string = "aa"
		regex = "a*"
		expected = True
		result = main(string, regex)
		self.assertEqual(expected, result)

	def testE(self):
		string = "aa"
		regex = ".*"
		expected = True
		result = main(string, regex)
		self.assertEqual(expected, result)

	def testF(self):
		string = "ab"
		regex = ".*"
		expected = True
		result = main(string, regex)
		self.assertEqual(expected, result)

	def testG(self):
		string = "aab"
		regex = "c*a*b"
		expected = True
		result = main(string, regex)
		self.assertEqual(expected, result)


if __name__ == '__main__':
	ut.main()
