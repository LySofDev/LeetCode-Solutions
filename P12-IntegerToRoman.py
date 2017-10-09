'''
12. Integer To Roman

Given an integer, convert it to a roman numeral.

Input is guaranteed to be within the range from 1 to 3999.
'''
import unittest as ut


def main(n):
	'''
	n: Integer -> Positive number to convert
	return: String -> Roman numeral representing number
	'''
	# If number less than 1 or greater than 3999
	if n < 1 or n > 3999:

		# Raise standard error with message
		raise ValueError("Number out of range.")

	# Initialize roman numeral to empty string
	rn = ""

	# Initiate index for roman numerals
	ns = [
		1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1
	]

	# Initiate roman numerals
	rns = [
		"M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"
	]

	# Iterate over roman numeral indexes
	for i in range(len(ns)):

		# Extract quotient from number
		q = n // ns[i]

		# While quotient still has value
		while q:

			# Append value to roman numeral
			rn += rns[i]

			# Subtract one from quotient
			q -= 1

		# Set number to remainder
		n = n % ns[i]

	# Return roman numeral
	return rn


class Tests (ut.TestCase):

	def testA(self):
		numbers = [
			1093, 282, 2471, 417, 3272, 477, 3643, 3771, 1019
		]

		romans = [
			"MXCIII", "CCLXXXII", "MMCDLXXI", "CDXVII", "MMMCCLXXII",
			"CDLXXVII", "MMMDCXLIII", "MMMDCCLXXI", "MXIX"
		]

		for i in range(len(numbers)):
			self.assertEqual(main(numbers[i]), romans[i])

	def testB(self):
		with self.assertRaises(ValueError):
			main(-1)

	def testC(self):
		with self.assertRaises(ValueError):
			main(4000)


if __name__ == '__main__':
	ut.main()
