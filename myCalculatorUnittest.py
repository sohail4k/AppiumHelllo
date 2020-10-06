'''
Created on Oct 1, 2020

@author: v792499
'''
from myCalculator import mycalculator
import unittest


class testMyCalculator(unittest.TestCase):
    '''
    classdocs
    '''
    def setUp(self):
        self.calculator=mycalculator()
        
    def test_add(self):
        self.assertEqual( self.calculator.add(6, 7),13,'add went fine')
        print(f'all went')
    def test_subtract(self):
        self.assertEqual(self.calculator.subtract(20,31),-11)
    def test_multiply(self):
        self.assertEqual(self.calculator.multiply(4, 6),24)
    def test_divide(self):
        self.assertEqual(self.calculator.divide(63,3),21)
        
        

if __name__=='__main__':
    unittest.main()
        