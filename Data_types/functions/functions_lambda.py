def add_numbers(a, b):
   result=a+b
   return result
   # 🔽 Test Cases
print(add_numbers(2, 3))   # Expected: 5
print(add_numbers(10, 20)) # Expected: 30

#lambda
square = (lambda n:n**2)
# 🔽 Test Cases
print(square(4))   # Expected: 16
print(square(7))   # Expected: 49

# Write a lambda function to find the mxm of two numbers
maximum = (lambda n1,n2: n1 if n1>n2 else n2)
# 🔽 Test Cases
print(maximum(10, 20))  # Expected: 20
print(maximum(5, 3))    # Expected: 5

def sum_all(*args):
    return sum(args)
    # 🔽 Test Cases
print(sum_all(1, 2, 3))        # Expected: 6
print(sum_all(10, 20, 30, 40)) # Expected: 100

def find_max(*args):
    return max(args)
# 🔽 Test Cases
print(find_max(1, 5, 3))     # Expected: 5
print(find_max(10, 2, 8, 6)) # Expected: 10

def print_details(**kwargs):
    print(kwargs)
    print(kwargs.get("name"))
    print(kwargs.get("age"))

    # 🔽 Test Cases
print_details(name="Ammu", age=21)
# Expected:
# name Ammu
# age 21
#Write a function sum_values(**kwargs) that returns the sum of all values
def sum_values(**kwargs):
    if(kwargs.get("a")==10):
        return 
    pass


# 🔽 Test Cases
print(sum_values(a=10, b=20, c=30))  # Expected: 60
print(sum_values(x=5, y=15))         # Expected: 20

