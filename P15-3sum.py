'''
15. 3sum

Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note: The solution set must not contain duplicate triplets.

For example, given array S = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
'''
import unittest as ut


def main():
	'''
	return: None
	'''
	# SOLUTION
	pass


class Tests (ut.TestCase):

	def testA(self):
		ns = [-1, 0, 1, 2, -1, -4]
		expected = [[-1, 0, 1], [-1, -1, 2]]
		result = main(ns)
		self.assertEqual(expected, result)


if __name__ == '__main__':
	ut.main()
