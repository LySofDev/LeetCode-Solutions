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


def same(xs, ys):
    '''
    xs: Integer[] -> List of integers
    ys: Integer[] -> List of integers
    return: Boolean -> True if both lists contain the same integers
    '''
    # Duplicate first list
    xs = xs[:]
    
    # Duplicate second list
    ys = ys[:]
    
    # While both list still contain items
    while len(xs) and len(ys):

        # Remove last item from first list
        x = xs.pop()
        
        # Try to find the index of x in the second list
        try:
            i = ys.index(x)
            
        # Return False if x doesn't exst in ys
        except ValueError:
            return False
        
        # Remove x from the second list
        ys.pop(i)
    
    # Return true if both lists are empty, False otherwise
    return len(xs) == len(ys)
    
    


def main(ns):
    '''
    ns: Integer[] -> List of numbers
    return: Integer[][3] -> List of triplets
    '''
    # Initialize triplets to empty list
    ts = []
    
    # Initialize index of x to 0
    x = 0
    
    # While at least two items remain after x
    while x < len(ns) - 2:
        
        # Initialize index of y to one after index of x
        y = x + 1
        
        # While at least on item remains after y
        while y < len(ns) - 1:
            
            # Initilize index of z to one after index of y
            z = y + 1
            
            # While an item remains in list
            while z < len(ns):
                
                # If the sum of x y and z is 0
                if not ns[x] + ns[y] + ns[z]:
                    
                    # Set new triplet to the values of x, y and z
                    nt = [ns[x], ns[y], ns[z]]
                    
                    # If new triplet doesn't exist in triplets
                    if not any(filter(lambda t: same(t, nt), ts)):
                        
                        # Append new triplet to triplets
                        ts.append(nt)
                    
                
                # Increment z index by 1
                z += 1
            
            # Increment y index by 1
            y += 1
            
        # Increment x index by 1
        x += 1
        
    # Return triplets
    return ts
        


class Tests (ut.TestCase):

    def testA(self):
        ns = [-1, 0, 1, 2, -1, -4]
        expected = [[-1, 0, 1], [-1, 2, -1]]
        result = main(ns)
        self.assertEqual(expected, result)

    def testB(self):
        ns = [-1, 2, 1]
        ms = [2, 1, -1]
        self.assertEqual(same(ns, ms), True)

    def testC(self):
        ns = [5, 2, 1]
        ms = [4, 2, 5]
        self.assertEqual(same(ns, ms), False)
        
    def testD(self):
        ns = [1, 2]
        ms = [1, 2, 3]
        self.assertEqual(same(ns, ms), False)

if __name__ == '__main__':
    ut.main()
