'''
4. Median Of Two Sorted Arrays

There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

Example 1:

nums1 = [1, 3]
nums2 = [2]

The median is 2.0

Example 2:

nums1 = [1, 2]
nums2 = [3, 4]

The median is (2 + 3)/2 = 2.5
'''
import unittest as ut


def main(nsx, nsy):
	# SOLUTION
	pass
	

class Tests (ut.TestCase):

	def testA(self):
		ns1 = [1, 3]
		ns2 = [2]
		expected = 2.0
		result = main(ns1, ns2)
		self.assertEqual(result, expected)

	def testB(self):
		ns1 = [1, 2]
		ns2 = [3, 4]
		expected = 2.5
		result = main(ns1, ns2)
		self.assertEqual(result, expected)
		
if __name__ == '__main__':
	ut.main()
