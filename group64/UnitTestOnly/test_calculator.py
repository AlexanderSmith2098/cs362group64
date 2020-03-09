import unittest
import calculator
import math
from decimal import *

#Must work on whole numbers, fractions, negative, large, and small

class TestCase(unittest.TestCase):
    def testmultiplication(self):
        input1a = 99999999999
        input1b = -99999999999
        expected1 = input1a * input1b
        input2a = -0.0000000001
        input2b = -0.0000000001
        expected2 = input2a * input2b
        input3a = 0
        input3b = 64
        expected3 = input3a * input3b
        self.assertEqual(expected1, calculator.multiplication(input1a,input1b))
        self.assertEqual(expected2, calculator.multiplication(input2a,input2b))
        self.assertEqual(expected3, calculator.multiplication(input3a,input3b))
        
    def testdivision(self):
        input1a = 99999999999
        input1b = -99999999999
        expected1 = input1a / input1b
        input2a = -0.0000000001
        input2b = -0.0000000001
        expected2 = input2a / input2b
        input3a = 0
        input3b = 64
        expected3 = input3a / input3b
        expected4 = False
        self.assertEqual(expected1, calculator.division(input1a,input1b))
        self.assertEqual(expected2, calculator.division(input2a,input2b))
        self.assertEqual(expected3, calculator.division(input3a,input3b))
        self.assertEqual(expected4, calculator.division(input3b,input3a))
        
    def testsquare_root(self):
        input1 = 99999999999
        expected1 = math.sqrt(input1)
        input2 = 0.0000000001
        expected2 = math.sqrt(input2)
        input3 = 64
        expected3 = math.sqrt(input3)
        expected4 = False
        self.assertEqual(expected1, calculator.square_root(input1))
        self.assertEqual(expected2, calculator.square_root(input2))
        self.assertEqual(expected3, calculator.square_root(input3))
        self.assertEqual(expected4, calculator.square_root(input3 * -1))

    def test_squareNum(self):
        # Partition testing variables
        input_zero = 0
        input_positive = 500
        input_negative = -495
        input_fraction = .7
        # Boundary testing variables
        input_posBoundary = 9999999999999999
        posExpected = 9999999999999999 * 9999999999999999
        input_negBoundary = -9999999999999999
        negExpected = -9999999999999999 * -9999999999999999
        input_beyondBoundary = 10000000000000000000
        # Bad input testing variable
        input_badInput = "dfjaldkf"

        self.assertEqual(0, calculator.squareNum(input_zero))
        self.assertEqual(250000, calculator.squareNum(input_positive))
        self.assertEqual(245025, calculator.squareNum(input_negative))
        # Almost equal utilized because of float representation not providing 1:1 correspondence with real life
        # calculation of decimal multiplication
        self.assertAlmostEqual(0.49, calculator.squareNum(input_fraction))
        # Boundary assert statements and error checking
        self.assertEqual(posExpected, calculator.squareNum(input_posBoundary))
        self.assertEqual(negExpected, calculator.squareNum(input_negBoundary))
        self.assertEqual("Error, number of digits in input too large", calculator.squareNum(input_beyondBoundary))
        self.assertEqual("Error, only numerical input allowed", calculator.squareNum(input_badInput))

    def test_multInverse(self):
        # Partition testing variables
        input_positive = 500
        input_negative = -495
        negExpected = -0.0020202
        input_fraction = .40
        # Boundary testing variables
        input_zero = 0
        input_atBoundary = 9999999999999999
        boundaryExpected = 1 / 9999999999999999
        input_beyondBoundary = 10000000000000000000
        # Bad character testing variable
        input_badInput = "dfjaldkf"
        
        self.assertEqual(0.002, calculator.multInverse(input_positive))
        # Almost equal assert utilized due to infinite repeating end sequence
        self.assertAlmostEqual(negExpected, calculator.multInverse(input_negative))
        self.assertEqual(2.5, calculator.multInverse(input_fraction))
        # Boundary assert statements
        self.assertEqual("Error, division by 0", calculator.multInverse(input_zero))
        self.assertEqual(boundaryExpected, calculator.multInverse(input_atBoundary))
        self.assertEqual("Error, number of digits in input too large", calculator.multInverse(input_beyondBoundary))
        self.assertEqual("Error, only numerical input allowed", calculator.multInverse(input_badInput))

    def test_fact(self):
        # Input variables to test normal use of fact function
        input_fraction = 0.34
        expectedfractionFact = 0.8922155
        input1 = 12
        input2 = 30
        # Boundary testing and error checking variables
        input3 = 100
        input_negative = -495
        inputZero = 0
        input_beyondBoundary = 101
        input_badInput = "dfjaldkf"

        # Almost equal used because gamma function for fractional factorial has infinite sequence of trailing numbers
        self.assertAlmostEqual(expectedfractionFact, calculator.fact(input_fraction))
        self.assertEqual(479001600, calculator.fact(input1))
        self.assertEqual(265252859812191058636308480000000, calculator.fact(input2))
        # Used math.factorial(), since the numerical representation is very long as expected value, and boundary asserts
        self.assertEqual(math.factorial(100), calculator.fact(input3))
        self.assertEqual("Non-negative numbers only", calculator.fact(input_negative))
        self.assertEqual(1, calculator.fact(inputZero))
        self.assertEqual("Overflow", calculator.fact(input_beyondBoundary))
        self.assertEqual("Error, only numerical input allowed", calculator.fact(input_badInput))

    def testabs(self):
        input1 = 99999999999
        expected1 = 99999999999
        input2 = -0.0000000001
        expected2 = 0.0000000001
        input3 = -300
        expected3 = 300
        self.assertEqual(expected1, calculator.absolute(input1))
        self.assertEqual(expected2, calculator.absolute(input2))
        self.assertEqual(expected3, calculator.absolute(input3))

    def testsin(self):
        input1 = 0
        expected1 = 0
        input2 = -(math.pi)
        expected2 = 0
        input3 = math.pi / 2
        expected3 = 1
        self.assertEqual(expected1, calculator.sin(input1))
        self.assertEqual(expected2, calculator.sin(input2))
        self.assertEqual(expected3, calculator.sin(input3))


    def testcos(self):
        input1 = 0
        expected1 = 1
        input2 = -(math.pi)
        expected2 = 1
        input3 = math.pi / 2
        expected3 = 0
        self.assertEqual(expected1, calculator.cos(input1))
        self.assertEqual(expected2, calculator.cos(input2))
        self.assertEqual(expected3, calculator.cos(input3))
        
        
if __name__ == '__main__':
    unittest.main()
