# def add_numbers(a, b):
#    result=a+b
#    return result
#    # 🔽 Test Cases
# print(add_numbers(2, 3))   # Expected: 5
# print(add_numbers(10, 20)) # Expected: 30

# #lambda
# square = (lambda n:n**2)
# # 🔽 Test Cases
# print(square(4))   # Expected: 16
# print(square(7))   # Expected: 49

# # Write a lambda function to find the mxm of two numbers
# maximum = (lambda n1,n2: n1 if n1>n2 else n2)
# # 🔽 Test Cases
# print(maximum(10, 20))  # Expected: 20
# print(maximum(5, 3))    # Expected: 5

# def sum_all(*args):
#     return sum(args)
#     # 🔽 Test Cases
# print(sum_all(1, 2, 3))        # Expected: 6
# print(sum_all(10, 20, 30, 40)) # Expected: 100

# def find_max(*args):
#     return max(args)
# # 🔽 Test Cases
# print(find_max(1, 5, 3))     # Expected: 5
# print(find_max(10, 2, 8, 6)) # Expected: 10

# def print_details(**kwargs):
#     print(kwargs)
#     print(kwargs.get("name"))
#     print(kwargs.get("age"))

#     # 🔽 Test Cases
# print_details(name="Ammu", age=21)
# # Expected:
# # name Ammu
# # age 21
# #Write a function sum_values(**kwargs) that returns the sum of all values
def sum_values(**kwargs):
    sum=0
    for value in kwargs.values():
        sum+=value
    return sum
    # 🔽 Test Cases
print(sum_values(a=10, b=20, c=30))  # Expected: 60
print(sum_values(x=5, y=15))         # Expected: 20

#last character of string
last_char=lambda s:s[-1]

print(last_char("python"))  # n
#filter even numbers

nums = [1, 2, 3, 4, 5, 6]
even_nums=list(filter(lambda num: True if num%2==0 else False,nums))
print(even_nums)  # [2, 4, 6]

data = [(1, 3), (2, 1), (4, 2)]
#sort list of tuples
sorted_data=sorted(data,key=lambda x:x[1])

print(sorted_data)  # [(2,1), (4,2), (1,3)]
