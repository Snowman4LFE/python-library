# -----------------------------------------------------------
# Demonstrates how to write helper library files using python
#
# (C) 2020 Kyle B. Vo, Virginia, USA
# Virginia Commonwealth University
# Society of bioinformatics
# Email thinhvo1101@gmail.com
# Github https://github.com/votb92/
# -----------------------------------------------------------
"""
| check if a number is even
|
| Parameters:
|    anInt (integer): an integer
|
| Returns:
|    boolean: true if anInt is even
"""
def isEven(anInt):
    return anInt%2 == 0

"""
| check if a number is odd
|
| Parameters:
|    anInt (integer): an integer
|
| Returns:
|    boolean: true if anInt is odd
"""
def isOdd(anInt):
    return not isEven(anInt)

"""
| getting the last digit of a number
|
| Parameters:
|    anInt (integer): an integer
|
| Returns:
|    integer: the last digit
"""
def lastDigit(anInt):
    return anInt%10