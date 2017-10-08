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
	# While both orignal text and regex still have characters
	while len(cs) and len(r):

		# Character matched if the first regex character matches the first
		# character in the original text or the first regex character is .
		cm = r[0] == cs[0] or r[0] == '.'

		# Multiple permited if another character remains in the regex and that
		# character is *
		mp = len(r) > 1 and r[1] == '*'

		# if Character matched and multiple permited
		if cm and mp:

			# Remove first character from original text
			cs = cs[1:]

		# If character matched but not multiple permited
		elif cm and not mp:

			# Remove first character from original text
			cs = cs[1:]

			# Remove first character from regex
			r = r[1:]

		# If character not matched but multiple permited
		elif not cm and mp:

			# Remove first two characters from regex
			r = r[2:]
			
		# If character not matched and multiple not permited
		else:

			# Original text doesn't match regex
			return False

	# Return true if no characters remain in original text
	return not len(cs)


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
