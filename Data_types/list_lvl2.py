# Find sum of all elements

# Find maximum number

# Reverse a list

# Count how many times a number appears

# Sort a list

lst=[10,20,30]
sum=0
for num in lst:
    sum=sum+num
print(sum)

#mxm number
lst=[10,20,30]
maximum=lst[0]
large=0
for num in lst:
    if num>maximum:
        large=num
print("maximum number is",large)
#reverse a list
lst=[10,20,30,45]
reversed=lst[::-1]
print(reversed)
#count 
lst=[10,15,20,20,35,40,15,20]
counted=lst.count(20)
print("count of number",counted)

#sorted list
lst=[20,30,10,36,23,60]
print(sorted(lst))

# Remove duplicates from list

# Merge two lists

# Find second largest number

# Find common elements between two lists

# Create list of squares from 1 to 10
lst=[10,20,10,30,20,30,56,89,12]
result_set=set(lst)
print(result_set)
#merging
lst1=[20,35,50,10]
lst2=[30,40]
merged=lst1+lst2
print(merged)
#secnd largest
lst=[25,30,40,50,10]
lst.sort()
print(lst[3])
#common elements
lst1=[10,15,20,35,20]
lst2=[10,15,30,44]
common=set(lst1)
common1=set(lst2)
print(common.intersection(common1))
