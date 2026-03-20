# *
# **
# ***
# ****
#print this output
for r in range(1,6):
    for c in range(1,r):
        print("*",end="")
    print()


# #****
# ***
# **
# *

#print reverse pattern
for r in range(5,0,-1):
    for c in range(1,r):
        print("*",end="")
    print()

#count vowels in astring
def count_vowels(s):
    vowels="aeiouAEIOU"
    count=0
    for ch in s:
        if ch in vowels:
            count+=1
    return count
   
# 🔽 Test Cases
print(count_vowels("hello"))    # Expected: 2
print(count_vowels("AEIOU"))    # Expected: 5
print(count_vowels("python"))   # Expected: 1
#factorial of a number
def factorial(n):
    fact=1
    for i in range(1,n+1):
        fact=fact*i
    return fact
# 🔽 Test Cases
print(factorial(5))   # Expected: 120
print(factorial(3))   # Expected: 6
print(factorial(0))   # Expected: 1
#palindrome of a number

def is_palindrome(n):
    result=0
    while(n!=0):
        digit=n%10
        result=result*10+digit
        n=n//10
    return result
# 🔽 Test Cases
print(is_palindrome(121))   # Expected: Yes
print(is_palindrome(123))   # Expected: No
print(is_palindrome(444))   # Expected: Yes



