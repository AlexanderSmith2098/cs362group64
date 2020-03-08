import math

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
    
def absolute(x):
    return abs(x)
    
def sin(x):
    return math.sin(x)
    
def cos(x):
    return math.cos(x)