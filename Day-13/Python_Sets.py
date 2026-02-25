set1 = {2,4,"Hello",2,"abhinav","hello",2,4}

print(set1)
print(type(set1))
print(len(set1))

list1 = [2,4,2,7,4,4,5,35,7,3,8,5,23,9,6,9,5,89,4,3,1,2]

# Converting list to set to remove duplicates 
# This will gave the Unique elements of the list

set2 = set(list1)
print(set2)
print(len(set2))

set1.add("Python")
print(set1)

'''Both discard and remove are used to remove an element from the set.
the difference is that discard will not give an error if the element is not present in the set, 
while remove will give an error if the element is not present in the set.'''

set1.discard("Hello")

set1.remove("abhinav") # This will give error if the element is not present in the set

print(set1)

if "Python" in set1:
    print(True)
else:
    print(False)


set3 = {1,2,3,4,5}
set4 = {4,5,6,7,8}

# Union of two sets
print(set3 | set4) # This will give the union of two sets

print(set3.union(set4)) # This will also give the union of two sets

# Intersection of two sets
print(set3 & set4) # This will give the intersection of two sets
print(set3.intersection(set4)) # This will also give the intersection of two sets

# Difference of two sets
print(set3 - set4) # This will give the difference of two sets
print(set3.difference(set4)) # This will also give the difference of two sets

# Symmetric Difference of two sets (Union - Intersection)
print(set3 ^ set4) # This will give the symmetric difference of two sets
print(set3.symmetric_difference(set4)) # This will also give the symmetric difference of two sets



