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


def safely_append_character(zz, cs, i):
    '''
    zz: String -> Resulting text
    cs: String -> Original text
    i: Integer -> Character index
    return: String -> Resulting text with the appended character
    '''
    try:
        return zz + cs[i]
    except IndexError:
        return zz


def main(cs, rs):
    '''
    cs: String -> Original text
    rs: Integer -> Number of rows
    return: String -> Original text zigzaged
    '''
    # Initiate zigzag result to an empty string
    zz = ""
    
    # Set step length to number of rows minus 1 times 2
    x = (rs - 1) * 2
    
    # Iterate over each row
    for r in range(rs):
        
        # Set character index to current row
        i = r
        
        # Set downwards step to step length minus current row times 2
        y = x - 2 * r
        
        # Set upwards step to step length minus downward step
        z = x - y
        
        # Append first character of row to resulting string
        zz = safely_append_character(zz, cs, i)
        
        # While index is within bounds of given string
        while i < len(cs):
            
            # If downwards step is greater than 0
            if y > 0:
                
                # Increment index by downward step
                i += y
                
                # Append character to resulting string
                zz = safely_append_character(zz, cs, i)

            # If upward step is greater than 0
            if z > 0:
                
                # Increment index by upward step
                i += z
                
                # Append character to resulting string
                zz = safely_append_character(zz, cs, i)
                
    # Return resulting string
    return zz


class Tests (ut.TestCase):

    def testA(self):
        original = "PAYPALISHIRING"
        rows = 3
        expected = "PAHNAPLSIIGYIR"
        result = main(original, rows)
        self.assertEqual(expected, result)
        
    def testB(self):
        original = "THEQUICKBROWNFOX"
        rows = 5
        expected = "TBHKRXECOOQIWFUN"
        result = main(original, rows)
        self.assertEqual(expected, result)


if __name__ == '__main__':
    ut.main()
