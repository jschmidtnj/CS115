'''
Created on Mar 1, 2015
Last modified on 10/18/2017

@author: Brian Borowski & Joshua Schmidt jschmid3@stevens.edu
Pledge:    I pledge my honor that I have abided by the Stevens Honor System -Joshua Schmidt

CS115 - Hw 6 Test Script
'''
import unittest
import hw6

class Test(unittest.TestCase):

    def test01(self):
        sequence = '0' * 64
        compress = hw6.compress(sequence)
        self.assertEqual(compress, '1111100000111110000000010')
        uncompress = hw6.uncompress(compress)
        self.assertEqual(uncompress, sequence)
        self.assertAlmostEqual(hw6.compression(sequence), 0.390625, 4)

    def test02(self):
        sequence = '01' * 32
        compress = hw6.compress(sequence)
        self.assertEqual(compress, '00001000010000100001000010000100001000010000100001000010000100001000010000100001000010000100001000010000100001000010000100001000010000100001000010000100001000010000100001000010000100001000010000100001000010000100001000010000100001000010000100001000010000100001000010000100001000010000100001000010000100001000010000100001')
        uncompress = hw6.uncompress(compress)
        self.assertEqual(uncompress, sequence)
        self.assertAlmostEqual(hw6.compression(sequence), 5.0, 4)

    def test03(self):
        sequence = '10' * 32
        compress = hw6.compress(sequence)
        self.assertEqual(compress, '0000000001000010000100001000010000100001000010000100001000010000100001000010000100001000010000100001000010000100001000010000100001000010000100001000010000100001000010000100001000010000100001000010000100001000010000100001000010000100001000010000100001000010000100001000010000100001000010000100001000010000100001000010000100001')
        uncompress = hw6.uncompress(compress)
        self.assertEqual(uncompress, sequence)
        self.assertAlmostEqual(hw6.compression(sequence), 5.078125, 4)

    def test04(self):
        sequence = '0' * hw6.MAX_RUN_LENGTH + '1' * hw6.MAX_RUN_LENGTH + '0' * (64 - 2 * hw6.MAX_RUN_LENGTH)
        compress = hw6.compress(sequence)
        self.assertEqual(compress, '111111111100010')
        uncompress = hw6.uncompress(compress)
        self.assertEqual(uncompress, sequence)
        self.assertAlmostEqual(hw6.compression(sequence), 0.234375, 4)

    def test05(self):
        sequence = '0' * (hw6.MAX_RUN_LENGTH + 1) + '1' * (hw6.MAX_RUN_LENGTH + 1) + '0' * (64 - 2 * hw6.MAX_RUN_LENGTH - 2)
        compress = hw6.compress(sequence)
        self.assertEqual(compress, '111110000000001111110000000001')
        uncompress = hw6.uncompress(compress)
        self.assertEqual(uncompress, sequence)
        self.assertAlmostEqual(hw6.compression(sequence), 0.46875, 4)

    def test06(self):
        sequence = '1' * hw6.MAX_RUN_LENGTH + '0' * hw6.MAX_RUN_LENGTH + '1' * (64 - 2 * hw6.MAX_RUN_LENGTH)
        compress = hw6.compress(sequence)
        self.assertEqual(compress, '00000111111111100010')
        uncompress = hw6.uncompress(compress)
        self.assertEqual(uncompress, sequence)
        self.assertAlmostEqual(hw6.compression(sequence), 0.3125, 4)
        
    #MAKE 2 test functions!
    def test07(self):
        """tested one random checkerboard"""
        sequence = '01' * 8
        compress = hw6.compress(sequence)
        self.assertEqual(compress, '00001000010000100001000010000100001000010000100001000010000100001000010000100001')
        uncompress = hw6.uncompress(compress)
        self.assertEqual(uncompress, sequence)
        self.assertAlmostEqual(hw6.compression(sequence), 5.0, 4)
        
    def test08(self):
        """tested a second different checkerboard"""
        sequence = '0100100111'*8
        compress = hw6.compress(sequence)
        self.assertEqual(compress, '000010000100010000010001000011000010000100010000010001000011000010000100010000010001000011000010000100010000010001000011000010000100010000010001000011000010000100010000010001000011000010000100010000010001000011000010000100010000010001000011')
        uncompress = hw6.uncompress(compress)
        self.assertEqual(uncompress, sequence)
        self.assertAlmostEqual(hw6.compression(sequence), 3.0, 4)
        
    def test09(self):
        """testing the penguin"""
        sequence =  "00011000"+"00111100"*3 + "01111110"+"11111111"+"00111100"+"00100100"
        compress = hw6.compress(sequence)
        self.assertEqual(compress, '00011000100010100100001000010000100001000001100110000010100000010001000010000001000100000100010')
        uncompress = hw6.uncompress(compress)
        self.assertEqual(uncompress, sequence)
        self.assertAlmostEqual(hw6.compression(sequence), 1.484375, 4)

    def test10(self):
        """testing the smile"""
        sequence = "0"*8 + "01100110"*2 + "0"*8 + "00001000" + "01000010" + "01111110" + "0"*8
        compress = hw6.compress(sequence)
        self.assertEqual(compress, '0100100010000100001000010000100001000010011010000100100000010010000001000100011001001')
        uncompress = hw6.uncompress(compress)
        self.assertEqual(uncompress, sequence)
        self.assertAlmostEqual(hw6.compression(sequence), 1.328125, 4)
    
    def test11(self):
        """testing the five"""
        sequence = "1"*9 + "0"*7 + "10000000"*2 + "1"*7 + "0" + "00000001"*2 + "1"*7 + "0"
        compress = hw6.compress(sequence)
        self.assertEqual(compress, '00000010010011100001001110000100111001110100000001001110100000001')
        uncompress = hw6.uncompress(compress)
        self.assertEqual(uncompress, sequence)
        self.assertAlmostEqual(hw6.compression(sequence), 1.015625, 4)
        
if __name__ == "__main__":
    unittest.main()
