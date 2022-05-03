# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.

import math

def prime_num_sum(num):

    prime_list = [2, 3, 5]

    for i in range(7, num + 1, 2):

        isprime = True
        
        for j in range(3, int(1 + math.sqrt(i))):

            if i % j == 0:
                isprime = False
                break
        
        if isprime:
            prime_list.append(i)

    return sum(prime_list)

print(prime_num_sum(2000000))