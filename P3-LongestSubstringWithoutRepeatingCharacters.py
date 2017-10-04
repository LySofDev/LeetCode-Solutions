'''
Longest Substring Without Repeating Characters

Given a string, find the length of the longest substring without repeating characters.

Examples:

Given "abcabcbb", the answer is "abc", which the length is 3.

Given "bbbbb", the answer is "b", with the length of 1.

Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
'''
import unittest as ut


def main(cs):
	# Set unique characters to empty list
	ucs = []
	
	# Set resulting length to 0
	rl = 0
	
	# Iterate over each character in string
	for c in cs:
		
		# If character already in unique character list
		if c in ucs:
			
			# If length of unique character list longer than current
			# resulting length
			if len(ucs) > rl:
				
				# Set resulting length to unique character list
				rl = len(ucs)
				
			# Reset unique character list with current character
			ucs = [c]
			
		# If character not included in unique character list
		else:
			
			# Insert character into unique character list
			ucs.append(c)
	
	# Return value of resulting length
	return rl
			
	

class Tests (ut.TestCase):

	def testA(self):
		string = "abcabcbb"
		expected = 3
		result = main(string)
		self.assertEqual(result, expected)
		
	def testB(self):
		string = "bbbbb"
		expected = 1
		result = main(string)
		self.assertEqual(result, expected)
		
	def testC(self):
		string = "pwwkew"
		expected = 3
		result = main(string)
		self.assertEqual(result, expected)


if __name__ == '__main__':
	ut.main()
