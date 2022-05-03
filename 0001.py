#If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23. 
#Find the sum of all the multiples of 3 or 5 below 1000.

def sum_of_multiples(range_num, multiple1, multiple2):

    list = []

    for i in range(0,range_num):
        
        if i % multiple1 == 0 or i % multiple2 == 0:
            list.append(i)
    
    return sum(list)

print(sum_of_multiples(1000, 3, 5))
