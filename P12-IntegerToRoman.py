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

	def testAll(self):
		numbers = [
			1093, 282, 2471, 417, 3272, 477, 3643, 3771, 1019
		]

		romans = [
			"MXCIII", "CCLXXXII", "MMCDLXXI", "CDXVII", "MMMCCLXXII",
			"CDLXXVII", "MMMDCXLIII", "MMMDCCLXXI", "MXIX"
		]

		for i in range(len(numbers)):
			self.assertEqual(main(numbers[i]), romans[i])


if __name__ == '__main__':
	ut.main()
