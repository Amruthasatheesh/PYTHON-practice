a = 10
b = 25
c = 15
#Find largest of three numbers
if a>b and a>c:
    largest=a
elif b>a and b>c:
    largest=b
else:
    largest=c
print(largest)
#Check if a year is leap year
#Hint: divisible by 4, 100, 400
# year=int(input("enter the year:"))
# if (year%400==0) or (year%4==0 and year%100!=0):
#     print("leap year")
# else:
#     print("not an leap year")
#Check if a character is vowel or consonant
ch = 'a'
vowel = "aeiouAEIOU"

if ch in vowel:
    print("Vowel")
else:
    print("Consonant")
#ATM,Success" if enough balance
#Otherwise "Insufficient balance"
balance = 5000
withdraw = 6000
if balance>withdraw:
    print("enough balance")
else:
    print("insufficient balance")
#predict output
x = None
if x:
    print("Yes")
else:
    print("No") #ans=yes

x = ""
if not x:
    print("Empty") #false 

