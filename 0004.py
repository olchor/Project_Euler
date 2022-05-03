# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

def palindrome(num1,num2):

    palindrome_list = []

    for i in range(num1,num2):
        
        for j in range(num1,num2):
            
            num = i * j
            num_str = str(num)

            if num_str == num_str[::-1]:
                palindrome_list.append(num)
    
    return max(palindrome_list)

print(palindrome(100,999))
