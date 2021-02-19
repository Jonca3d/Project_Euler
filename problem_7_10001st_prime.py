"""
Problem 7


By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?

"""

import math

number = 5

x = 2
prime_number = 3



while(x < 10001):
    for i in range(2, int(math.sqrt(number))+1):
        if number % i == 0:
            # print(i)
            break
        if i == int(math.sqrt(number)):
            x += 1
            prime_number = number
    print(x)
    number += 1

print(f'x: {x}\tprime: {prime_number}')

print(math.sqrt(5))