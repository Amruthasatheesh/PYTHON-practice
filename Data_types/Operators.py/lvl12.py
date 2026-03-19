a = 5
b = 2
print(a ** b + a // b)#27
# Write a program:
# Check if a number is even using %

# num=int(input("enter the number:"))
# if num%2==0:
#     print("even")
# else:
#     print("odd")

# print(10 > 5 and 5 > 2)#true
# print(10 > 5 and 5 < 2)#false
# 25 in data
data = [10, 20, 30, 40]

if 25 in data:
    print("yes")
else:
    print("no")
# 40 not in data
if 40 not in data:
    print("ys")
else:
    print("no")

# a is b

# a is c

a = [1,2]
b = [1,2]
c = a
if a is b:
    print("true")
else:
    print("false")
if a is c:
    print("true")
else:
    print("false")
#predict the output
print(5 > 3 > 1)#true

print(True + True * False)#1

a = 10      #t         #f
print(a > 5 or a < 2 and a == 10)#True(should follow the precedence rule and>or)

x = None
print(x is None)#t
print(x == None)#f
#find the mistake here
a = [1,2,3]
b = [1,2,3]
if a is b:
    print("Same")
else:
    print("Different") #ans:different
a = [1,2,3]
b = a
c = a.copy() #ans is c=[1,2,3] but independent and not same object like other var a,b
#predict the output

print(a is b, a is c)#t,f
print(True + False * 10)#1
#
a = [1,2,3]
b = a
c = [1,2,3]

print(a == c, a is c)#t,f
print(b == a, b is a)#t,t