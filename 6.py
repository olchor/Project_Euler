def diff_sumsq_sqsum(num):

    a = 0
    b = 0

    for i in range(1,num+1):

        a = a + i**2
        b = b + i

    b = b**2
    return b - a

print(diff_sumsq_sqsum(100))