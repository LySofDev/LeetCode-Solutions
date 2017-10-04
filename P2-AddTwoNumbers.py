'''
You are given two non-empty linked lists representing two non-negative 
integers. The digits are stored in reverse order and each of their nodes
contain a single digit. Add the two numbers and return it as a linked 
list.

You may assume the two numbers do not contain any leading zero, except 
the number 0 itself.

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
'''
import unittest as ut


def safely_get(numbers, index):
	try:
		return numbers[index]
	except IndexError:
		return 0


def main(nsx, nsy):
	# Set limit to length of longest list
	if len(nsx) > len(nsy):
		limit = len(nsx)
	else:
		limit = len(nsy)
		
	# Set index to 0
	index = 0
	
	# Set carry to 0
	carry = 0
	
	# Set sum list to empty list
	nss = []
	
	# While numbers still exist in either list
	while index < limit:
		
		# Get digit by index or 0 if out of bounds
		nx = safely_get(nsx, index)
		ny = safely_get(nsy, index)
		
		# Increment index by 1
		index += 1
		
		# Get digit sum with carry
		ns = nx + ny + carry
		
		# If sum is two digits
		if ns > 9:
			
			# Append last digit to result list
			nss.append(ns % 10)
			
			# Set first digit as carry value
			carry = ns // 10
			
		# If sum is one digit
		else:
			
			# Append digit to result list
			nss.append(ns)
			
			# Set carry value to 0
			carry = 0
			
	# Return resulting list
	return nss
			

class Tests (ut.TestCase):
	
	def testA(self):
		listA = [2, 4, 3]
		listB = [5, 6, 4]
		expected = [7, 0, 8]
		solution = main(listA, listB)
		self.assertEqual(solution, expected)
		
		
if __name__ == '__main__':
	ut.main()
