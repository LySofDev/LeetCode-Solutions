'''
12. Integer To Roman

Given an integer, convert it to a roman numeral.

Input is guaranteed to be within the range from 1 to 3999.
'''
import unittest as ut


def main():
	'''
	return: None
	'''
	# SOLUTION
	pass


class Tests (ut.TestCase):

	def setUp(self):
		self.numbers = [
			1093, 282, 2471, 417, 3272, 477, 3643, 3771, 1019
		]
		self.expected = [
			"MXCIII", "CCLXXXII", "MMCDLXXI", "CDXVII", "MMMCCLXXII",
			"CDLXXVII", "MMMDCXLIII", "MMMDCCLXXI", "MXIX"
		]

	def testAll(self):
		for i in range(len(self.numbers)):
			number = self.numbers[i]
			expected = self.expected[i]
			result = main(number)
			self.assertEqual(expected, result)


if __name__ == '__main__':
	ut.main()
