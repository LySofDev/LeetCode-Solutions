'''
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
'''
import unittest as ut


def main(nsx, nsy):
	pass


class Tests (ut.TestCase):
	
	def testA(self):
		listA = [2, 4, 3]
		listB = [5, 6, 4]
		expected = [7, 0, 8]
		solution = main(listA, listB)
		self.assertEqual(solution, expected)
		
		
if __name__ == '__main__':
	ut.main()
