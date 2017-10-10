'''
14. Longest Common Prefix

Write a function to find the longest common prefix string amongst an array of strings.
'''
import unittest as ut


def main(ss):
	'''
	ss: String[] -> List of strings
	return: String -> Longest common prefix
	'''
	# Initiate longest common prefix to an empty string
	lcp = ""

	# Set character index to 0
	i = 0

	# Set limit to the shortest length of strings
	l = min(map(lambda s: len(s), ss))

	# While character index is less than length of shortest string
	while i < l:

		# Get the current character with the character index
		cc = ss[0][i]

		am = True

		for s in ss:

			if s[i] != cc:

				am = False

		if am:

			lcp += cc

			i += 1

		else:

			break

	# Return the longest common prefix
	return lcp


class Tests (ut.TestCase):

	def testA(self):
		strings = [ "hello", "hell", "helicopter" ]
		expected = "hel"
		result = main(strings)
		self.assertEqual(expected, result)

	def testB(self):
		strings = [ "ruins", "run", "rum" ]
		expected = "ru"
		result = main(strings)
		self.assertEqual(expected, result)

	def testC(self):
		strings = [ "hi", "high", "higgs" ]
		expected = "hi"
		result = main(strings)
		self.assertEqual(expected, result)


if __name__ == '__main__':
	ut.main()
