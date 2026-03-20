# Print numbers from 1 to 20, stop when number is 15 (break)
for i in range(1,21):
    if i==15:
        break
    print(i)

# Print numbers from 1 to 20, skip multiples of 3 (continue)
for i in range(1,21):
    if i%3==0:
        continue
    print(i)

# Ask user input repeatedly until they enter "exit"
while True:
    user_input=input("enter something here:")
    if user_input=="exit":
     print("the program stopped/exitted here ")
    break
print("you entered this here",user_input)



# Find first number divisible by both 3 and 5 between 1–100
for i in range(1,101):
    if i%3==0 and i%5==0:
        break
print("divisible by both 3 and 5 is",i)#divisible by both 3 and 5 is 15

# Print all numbers except those divisible by 2 and 5
num=int(input("enter the number:"))
for i in range(1,num+1):
    if i%2==0 and i%5==0:
        continue
    print(i)

