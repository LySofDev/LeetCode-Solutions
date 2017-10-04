'''
1. Two Sum

Given an array of integers, return indices of the two numbers such that they add
up to a specific target.

You may assume that each input would have exactly one solution, and you may not
use the same element twice.
'''
import unittest as ut


def main(numbers, target):
	# Set starting indexes
	x, y = [0, 1]
	
	# While at least two numbers remain
	while x < (len(numbers) - 1):
		nx = numbers[x]
		
		# While at least one number remains
		while y < (len(numbers) - (x + 1)):
			ny = numbers[y]
			
			# Return indexes if sum of numbers equals target
			if nx + ny == target:
				return [x, y]
				
			# Increment y index
			y += 1
			
		# Increment x index
		x += 1
    
    
class Tests (ut.TestCase):

    def testA(self):
        numbers = [2, 7, 11, 15]
        target = 9
        expected_result = [0, 1]
        solution_result = main(numbers, target)
        self.assertEqual(solution_result, expected_result)


if __name__ == '__main__':
    ut.main()
