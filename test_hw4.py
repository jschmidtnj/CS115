'''
Created on Oct 3, 2017

@author: jschmid3@stevens.edu
Pledge:    I pledge my honor that I have abided by the Stevens Honor System -Joshua Schmidt

CS115 - test_hw4
'''
import unittest
import hw4

class Test(unittest.TestCase):
    """tests the pascal_triangle and pascal_row functions in hw4"""
    def test01(self):
        self.assertEqual(hw4.pascal_triangle(7), [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1], [1, 5, 10, 10, 5, 1], [1, 6, 15, 20, 15, 6, 1], [1, 7, 21, 35, 35, 21, 7, 1]])
    
    def test02(self):
        self.assertEqual(hw4.pascal_triangle(1), [[1], [1, 1]])
    
    def test03(self):
        self.assertEqual(hw4.pascal_triangle(0), [[1]])
        
    def test04(self):
        self.assertEqual(hw4.pascal_triangle(5), [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1], [1, 5, 10, 10, 5, 1]])
        
    def test05(self):
        self.assertEqual(hw4.pascal_triangle(3), [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1]])
        
    def test06(self):
        self.assertEqual(hw4.pascal_row(7), [1, 7, 21, 35, 35, 21, 7, 1])
    
    def test07(self):
        self.assertEqual(hw4.pascal_row(1), [1, 1])
    
    def test08(self):
        self.assertEqual(hw4.pascal_row(0), [1])
        
    def test09(self):
        self.assertEqual(hw4.pascal_row(5), [1, 5, 10, 10, 5, 1])
        
    def test10(self):
        self.assertEqual(hw4.pascal_row(3), [1, 3, 3, 1])

#etc.

if __name__ == "__main__":
    unittest.main()
    #on test2^^