# Create a set
st={200,300,100}

# Add element
st={200,300,100}
st.add(150)
print(st)

# Remove element
st={200,300,100}
st.pop()
print(st)


#  Medium

# Find union of two sets
st={200,300,100}
st2={250,200,300,400}
u=st.union(st2)
print(u)

# Find intersection
st={200,300,100}
st2={250,200,300,400}
u=st.intersection(st2)
print(u)

# Find difference
st={200,300,100}
st2={250,200,300,400}
u=st.difference(st2)
print(u)

# Tricky

# Remove duplicates from list using set
lst=[250,300,150,200,300,100]
res=set(lst)
print(res)

# Check if subset
st={200,300,100}
st2={250,200,300,400}
u=st.issubset(st2)
print(u)


# Find symmetric difference
st={200,300,100}
st2={250,200,300,400}
u=st.symmetric_difference(st2)
print(u)