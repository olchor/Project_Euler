#By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# What is the 10 001st prime number?
def prime_num(num):

    a = 15
    prime_list = [2, 3, 5, 7, 11, 13]

    while True:

        a += 2

        if a % 3 == 0 or a % 5 == 0 or a % 7 == 0 or a % 11 == 0 or a % 13 == 0:
            continue
        
        else:
            for j in range(15, a, 2):

                if a % j == 0:
                    break
                
                if j == a - 2:
                    prime_list.append(a)

        if len(prime_list) == num:
            return prime_list[-1]

print(prime_num(10001))
