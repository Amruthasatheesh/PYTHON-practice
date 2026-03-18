# Create a dictionary with name and age
person={"name":"haritha","age":23}

# Access value using key
print(person["age"])

# Add new key-value pair
person["place"]="plkd"
print(person)

# Medium

# Update value
person["age"]="24"
print(person)

# Delete a key
person.pop("age")
print(person)
# Loop through dictionary
for v in person.values():
    print(v)

#  Tricky

# Count frequency of characters in string
text="haritha"
counting={t:text.count(t)for t in text}
print(counting)

# Merge two dictionaries
person={"name":"haritha","age":23}
person2={"name":"meena","age":30}
rs=person|person2
print(rs)




# Find key with maximum value
# Convert two lists into dictionary