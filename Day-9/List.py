names = ["Alice", "Bob", "Charlie", "Diana"]

print(names)
print(type(names))
print(len(names))

names[0]= "Eve"

print(names[0])
print(names[2])
print(names[-1]) 

list1=[5, "Hello", 21.35, True, 254]

list2=[1,2,3,4,5]

list2.append(6)
list2.append(7)
print(list2)

list2.append([8, 9, 10]) # This will add the list [8, 9, 10] as a single element to the end of list2.
print(list2)

# extend is used to add multiple elements to the list. 
# It takes an iterable (like a list) and adds each element of the iterable to the end of the list.
list2.extend([11, 12, 13]) 
print(list2)

list3=[32,45,65,28,246,21,45,58,54,68]
list3.insert(3,100) # This will insert the value 100 at index 3. The element at index 3 and all subsequent elements will be shifted to the right.
print(list3)

list3.remove(45) # This will remove the first occurrence of the value 45 from the list. 
# If there are multiple occurrences of 45, only the first one is removed.
print(list3)

list3.pop() # This will remove the last element from the list and return it.
print(list3)

list3.pop(2) # This will remove the element at index 2 and return it.
print(list3)

print(max(list3))
print(min(list3))