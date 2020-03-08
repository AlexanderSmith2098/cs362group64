import unittest
import calculator

#Must work on whole numbers, fractions, negative, large, and small

class TestCase(unittest.TestCase):




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
