list1 = [2,4,2,7,4,4,5,35,7,3,8,5,23,9,6,9,5,89,4,3,1,2]

# To find the frequency of each element in the list
freq = {}
for values in list1:
    if values in freq:
        freq[values] += 1
    else:
        freq[values] = 1

print(freq)

s = "I am finding the frequency of each character in this string"
freq_char = {}

for char in s:
    if char in freq_char:
        freq_char[char] += 1
    else:
        freq_char[char] = 1
print(freq_char)