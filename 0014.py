# The following iterative sequence is defined for the set of positive integers:
# n → n/2 (n is even)
# n → 3n + 1 (n is odd)
# Using the rule above and starting with 13, we generate the following sequence:
# 13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
# It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.
# Which starting number, under one million, produces the longest chain?
# Note: Once the chain starts the terms are allowed to go above one million.

#Function that compare length of chains for every number below the one that is given
def collatz_start(end_num):
    longest_chain = 0
    
    for i in range(1, end_num):
        global chain_length
        chain_length = 1

        collatz_chain(i)

        if longest_chain < chain_length:
            longest_chain = chain_length
            starting_number = i

    return starting_number

#Function that checks how long is the chain
def collatz_chain(num):
    global chain_length
    chain_length += 1

    if num % 2 == 0:
        num = num / 2 
    else:
        num = num * 3 + 1
    
    if num == 1:
        return chain_length
    else:
        return collatz_chain(num)

print(collatz_start(1000000))