import unittest
import calculator
import math

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
