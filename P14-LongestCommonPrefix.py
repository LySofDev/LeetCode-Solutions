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
	# SOLUTION
	pass


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


if __name__ == '__main__':
	ut.main()
