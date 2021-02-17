"""
Problem 6

The sum of the squares of the first ten natural numbers is,
1**2 + 2**2 + ... + 10**2 = 385
The square of the sum of the first ten natural numbers is,
(1 + 2 + ... + 10)**2 = 55**2 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is
 3025 − 385 = 2640.
Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""

from fractions import Fraction


def sum_of_squares(amount_of_elements):
    am = amount_of_elements
    return Fraction(am*(am+1)*(2*am+1), 6)


def squared_sum(amount_of_elements):
    am = amount_of_elements
    return Fraction(am*(am+1), 2)**2


print(squared_sum(100)-sum_of_squares(100))