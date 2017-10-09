'''
11. Container With The Most Water

Given n non-negative integers a1, a2, ..., an, where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.

Note: You may not slant the container and n is at least 2.
'''
import unittest as ut


def main(hs):
	'''
	hs: Integer[] -> List of heights for lines
	return: Integer -> Greatest possible area
	'''
	# SOLUTION
	pass


class Tests (ut.TestCase):

	def testA(self):
		heights = [7, 6, 8, 5, 7, 5, 8, 6, 4, 5]
		expected = 45
		result = main(heights)
		self.assertEqual(expected, result)

	def testB(self):
		heights = [3, 5, 4, 3, 8, 4, 4, 3, 1]
		expected = 21
		result = main(heights)
		self.assertEqual(expected, result)


if __name__ == '__main__':
	ut.main()
