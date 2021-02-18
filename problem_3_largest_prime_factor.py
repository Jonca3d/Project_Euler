""""
Probelm 3
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""

import math

# x = 0
# flag = True
# number = 600851475143
# i = int(number / 2 + 1)
# while(flag):
#     k = 0
#     for j in range(2, int(math.sqrt(i))):
#         if i % j == 0:
#             k += 1
#             break
#         if number % i != 0:
#             break
        
#     if k == 0:
#         print(i)

#         if number % i == 0:
#             x = i
#             flag = False
#     i -= 1


# print('X: ' + str(x))


# number = 600851475143
# prime_numbers = []
# x = int(number / 2) + 1

# print(x)

# for i in range(2, 1000):
#     # print(i)
#     for j in range(2, i+1):
#         # print(j)
#         if j == i:
#             prime_numbers.append(i)
#         if i % j == 0:
#             break

# print(prime_numbers)
# print(math.sqrt(1000))
# print(int(math.sqrt(1000)))

# for i in range(1000, x):
#     for prime in prime_numbers:
#         # print(max(prime_numbers))
#         if i % prime == 0:
#             break
#         if prime > math.sqrt(i):
#             prime_numbers.append(i)
#             print(max(prime_numbers))

#             break

# print(prime_numbers)

number = 600851475143
flag = True

def largest_prime_factor():
    divisor = 2

    while(True):
        if number % divisor == 0:
            num = number / divisor
            print(f'Divisor: {divisor}')
            for i in range(2, int(math.sqrt(num))+1):
                if num % i == 0:
                    break
                if i == int(math.sqrt(num)):
                    print(f'I: {i}\tNUM: {num}\tDIVISOR: {divisor}')
                    print(f'SUM: {divisor*num}')
                    # flag = False
                    return num
        divisor += 1
                
print(f'RESULT: {int(largest_prime_factor())}')