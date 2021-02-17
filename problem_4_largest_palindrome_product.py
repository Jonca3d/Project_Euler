"""
Problem 4:


A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.

"""
from utilities import benchmark

# Num1 = 999    Num2 = 91
# Res = 90909

def reverse(string):
    string = string[::-1]
    return string

# @benchmark
def largest_palindrome_product():
    polindroms = []
    for i in reversed(range(100, 1000)):
        for j in reverse(range(100, 1000)):
            k = i * j
            if str(k) == reverse(str(k)):
                print(f'Num_1: {i}\tNum_2: {j}')
                if k > 10:
                    polindroms.append(k)
    return max(polindroms)


r = largest_palindrome_product()

print(f'Result: {r}')
