#The prime factors of 13195 are 5, 7, 13 and 29.
#What is the largest prime factor of the number 600851475143 ?

def prime_num(num):

    prime_list = []

    for i in range(17, num + 1, 2):

        if i % 3 == 0 or i % 5 == 0 or i % 7 == 0 or i % 11 == 0 or i % 13 == 0:
            continue
        
        else:
            for j in range(17, i, 2):

                if i % j == 0:
                    break
                
                if j == i - 2:
                    prime_list.append(i)

    return prime_list

def prime_factor(num, list):

    for i in range(1, len(list)):
       
        if num % list[i] == 0:
            factor = list[i]
    
    return factor

prime_factor_list = prime_num(100000)

print(prime_factor(600851475143, prime_factor_list))