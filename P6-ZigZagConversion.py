'''
6. ZigZag Conversion

The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of
rows like this: (you may want to display this pattern in a fixed font for better
 legibility)

P   A   H   N
A P L S I I G
Y   I   R

And then read line by line: "PAHNAPLSIIGYIR"
Write the code that will take a string and make this conversion given a number
of rows:

string convert(string text, int nRows);
convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR".
'''
import unittest as ut


def main(cs, r):
	# SOLUTION

	pass


class Tests (ut.TestCase):

	def testA(self):
		original = "PAYPALISHIRING"
		rows = 3
		expected = "PAHNAPLSIIGYIR"
		result = main(original, rows)
		self.assertEqual(expected, result)


if __name__ == '__main__':
	ut.main()
