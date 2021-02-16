""""
Probelm 3
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""

x = 0
flag = True
number = 600851475143
i = int(number / 2 + 1)
while(flag):
    k = 0
    for j in range(2, i):
        if i % j == 0:
            k += 1
            break
        if number % i != 0:
            break
        
    if k == 0:
        if number % i == 0:
            x = i
            flag = False
    i -= 1
    print(i)


print('X: ' + str(x))




