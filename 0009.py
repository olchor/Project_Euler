# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
# a^2 + b^2 = c^2
# For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

import math

def triplet(num):

    for a in range(1,int(num/3)):

        for b in range(a,num):
        
            c = a**2 + b**2
            sqrt_c = math.sqrt(c)
            
            if a + b + sqrt_c == num:
                
                return int(a * b * sqrt_c)

print(triplet(1000))
