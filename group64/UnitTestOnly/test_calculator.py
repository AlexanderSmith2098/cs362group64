import unittest
import calculator

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
        expected4 = input3b / input3a
        self.assertEqual(expected1, calculator.division(input1a,input1b))
        self.assertEqual(expected2, calculator.division(input2a,input2b))
        self.assertEqual(expected3, calculator.division(input3a,input3b))
        self.assertEqual(expected4, calculator.division(input3b,input3a))
        
    def testsquare_root(self):
        input1 = 99999999999
        expected1 = sqrt(input1)
        input2 = 0.0000000001
        expected2 = sqrt(input2)
        input3 = 64
        expected3 = sqrt(input3)
        expected4 = sqrt(input3 * -1)
        self.assertEqual(expected1, calculator.square_root(input1))
        self.assertEqual(expected2, calculator.square_root(input2))
        self.assertEqual(expected3, calculator.square_root(input3))
        self.assertEqual(expected4, calculator.square_root(input3 * -1))


    def testabs(self):
        input1 = 99999999999
        expected1 = 99999999999
        input2 = -0.0000000001
        expected2 = 0.0000000001
        input3 = -300
        expected3 = 300
        self.assertEqual(expected1, calculator.abs(input1))
        self.assertEqual(expected2, calculator.abs(input2))
        self.assertEqual(expected3, calculator.abs(input3))

    def testsin(self):
        input1 = 0
        expected1 = 2/5
        input2 = -3.14
        expected2 = -80
        input3 = 1000000000000
        expected3 = 1
        self.assertEqual(expected1, calculator.sin(input1))
        self.assertEqual(expected2, calculator.sin(input2))
        self.assertEqual(expected3, calculator.sin(input3))


    def testcos(self):
        input1 = 2
        expected1 = 2/5
        input2 = -10
        expected2 = -80
        input3 = 1000000000000
        expected3 = 1
        self.assertEqual(expected1, calculator.cos(input1))
        self.assertEqual(expected2, calculator.cos(input2))
        self.assertEqual(expected3, calculator.cos(input3))
