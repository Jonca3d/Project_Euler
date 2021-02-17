"""
Problem 5


2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

"""

from utilities import benchmark

@benchmark
def small_multiple():
    number = 20
    while(True):
        for i in range(1, 21):
            if number % i != 0:                
                break
            if i == 20:
                print(number)
                return
        number += 1


@benchmark
def small_multiple_v2():
    import math
    number = 1
    for i in range(1, 21):
        print(f'NUM: {number}')
        print(f'I: {i}\tGCD: {math.gcd(i, number)}\n----------')
        number *= i // math.gcd(i, number)
    print(number)


# small_multiple()
small_multiple_v2()