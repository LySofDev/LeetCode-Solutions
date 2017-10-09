'''
13. Roman To Integer

Given a roman numeral, convert it to an integer.

Input is guaranteed to be within the range from 1 to 3999.
'''
import unittest as ut


def main(rn):
	'''
	rn: String -> Roman numeral
	return: Integer -> Number represented by roman numeral
	'''
	# Initiate index for roman numerals
	ns = [
		1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1
	]

	# Initiate roman numerals
	rns = [
		"M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"
	]

	# Initialize resulting number to 0
	n = 0

	# Initialize the index to 0
	i = 0

	# While the index is less than the length of the roman numerl letters
	while i < len(rns):

		# If given roman numeral starts with letter
		if rn.startswith(rns[i]):

			# Add the value of the letter to the resulting number
			n += ns[i]

			# Remove the roman numeral letter from the given roman numeral
			rn = rn[len(rns[i]):]

		# If given roman numeral doesn't start with letter
		else:

			# Increment the index by 1
			i += 1

	# Return the resulting number
	return n


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
			self.assertEqual(main(romans[i]), numbers[i])


if __name__ == '__main__':
	ut.main()
