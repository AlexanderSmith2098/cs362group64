import math
from decimal import *

def multiplication(x,y):
    return x * y
    
def division(x,y):
    if y == 0:
        return False
    return x / y
    
def square_root(x):
    if x < 0:
        return False
    return math.sqrt(x)

def squareNum(x):
    # Checking that only a real number was typed
    if not (isinstance(x, float)):
        if not (isinstance(x, int)):
            return "Error, only numerical input allowed"
    # Restricting length of input
    if x > 9999999999999999 or x < -9999999999999999:
        return "Error, number of digits in input too large"
    # Return the square of the argument, x
    return x * x

def multInverse(x):
    # Checking that only a real number was typed
    if not (isinstance(x, float)):
        if not (isinstance(x, int)):
            return "Error, only numerical input allowed"
    # Restricting length of input
    if x > 9999999999999999 or x < -9999999999999999:
        return "Error, number of digits in input too large"
    # Division by 0 returns an error statement
    if x == 0:
        return "Error, division by 0"
    # Return the multiplicative inverse of the passed in argument, x
    return 1 / x

def fact(x):
    # Checking that only a real number was typed
    if not (isinstance(x, float)):
        if not (isinstance(x, int)):
            return "Error, only numerical input allowed"
    # Checking length of input is between 0 and 100 inclusive, otherwise returns an error statement
    if (x > 100):
        return "Overflow"
    if (x < 0):
        return "Non-negative numbers only"
    # If the passed in argument was an integer, utilizes while loop to calculate the factorial
    if (isinstance(x, int)):
        if (x == 0):
            return 1
        i = x
        while (i > 1):
            x = x * (i - 1)
            i -= 1
        return x
    # Otherwise, a floating/decimal point value was passed in, and so the gamma function is used instead
    else:
        return math.gamma(x + 1)

def absolute(x):
    return abs(x)
    
def sin(x):
    return math.sin(x)
    
def cos(x):
    return math.cos(x)