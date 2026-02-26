# Dictionaries in Python (Used as a Hash Map in other languages)

# A dictionary is a collection of key-value pairs.
# Each key is unique and maps to a value.
# Keys are typically strings or numbers, and values can be any data type.

dict1 = {"name": "Abhinav", "age": 25, "city": "New York",1:"Hello",10.21:"Python","key":True}

print(dict1)
print(type(dict1))
print(len(dict1))

dict2= {(1,2,3):"name": "Abhinav", "age": 25, "city": "New York",1:"Hello",10.21:"Python","key":True}

print(dict2)

# Accessing values in a dictionary using keys
print(dict1["name"])

# Adding a new key-value pair to the dictionary
dict1[5] = "New Value"
print(dict1)

# Removing a key-value pair from the dictionary using the del keyword
del dict1[1]
dict1.pop(10.21) # This will remove the key-value pair with key 10.21

print(dict1)