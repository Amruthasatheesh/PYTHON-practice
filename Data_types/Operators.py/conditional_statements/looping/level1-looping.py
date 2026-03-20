# Print numbers from 1 to 10 using for loop
for i in range(1,11):
    print(i)

# Print numbers from 10 to 1 using while loop
i=10
while(i>=1):
  print(i)
  i=i-1

# Print all even numbers between 1 and 50
for i in range(1,51):
   if i%2==0:
      print(i)

# Print all odd numbers between 1 and 50
for i in range(1,51,2):
   print(i)

# Find the sum of numbers from 1 to n (input from user)
num=int(input("enter the number:"))
sum=0
for i in range(1,num+1):
   sum=sum+i
print("sum of 1 to n",sum)
   
# Print multiplication table of a number (e.g., 5)
num=int(input("enter the number:"))
for i in range(1,11):
   mul=num*i
   print(mul)

# Count number of digits in a number
num=1345
counts=len(str(num))
print("count of a number is",counts)
# Reverse a number (e.g., 123 → 321)

num=int(input("enter number:"))
reverse=0
while(num!=0):
   digit=num%10
   reverse=reverse*10+digit
   num=num//10
print("reverse of a number is",reverse)


