# Create a tuple of 5 elements
tup=(20,30,40,50,10)

# Access first element
print(tup[0])

# Find length of tuple
length_tup=len(tup)
print(length_tup)

# Medium

# Convert tuple to list
tup=(20,30,40,50,10)
into_list=list(tup)
print(into_list)


# Count occurrences of element
tup=(20,30,40,50,10,30)
occurence=tup.count(30)
print(occurence)

# Find index of an element
tup=(20,30,40,50,10)
element_ind=tup.index(40)
print(element_ind)

#  Tricky

# Unpack tuple into variables
tup=(20,30,40,50,10)
a,b,c,d,e=tup
print(a)
print(b)
print(c)
print(d)
print(e)
# Swap two values using tuple
tup=(20,30)
a,b=tup
tupe=b,a
print(tupe)

# Convert list into tuple
lst=[100,200,450]
res=tuple(lst)
print(res)