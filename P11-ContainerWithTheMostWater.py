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
	# Initialize maximum area to 0
	ma = 0

	# Initialize left index to 0
	li = 0

	# Initialize right index to last possible index
	ri = len(hs) - 1

	# While left index is less than right index
	while li < ri:

		# Width is equal to the difference between left and right index
		w = ri - li

		# Height is shortest length between left and right height
		h = min(hs[li], hs[ri])

		# If left height is shorter than right height
		if h == hs[li]:

			# Increment left index by one
			li += 1

		# If right height is shorter than left height
		else:

			# Decrement right index by one
			ri -= 1

		# Area is equal to width times height
		a = w * h

		# Max height is greatest of area and maximum area
		ma = max(ma, a)

	# Return maximum area
	return ma


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
