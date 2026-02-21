name="nitish"
grade='A+'
company="Maurya Software"
introduction="""My name is nitish and I am a software developer. I have been working in the industry for 5 years. 
I have a passion for coding and I am always looking for new challenges. 
I am a quick learner and I am always willing to learn new technologies."""

print(name)

name1="Nitish Maurya"
name1+=" is a software developer."

print(name1[4])
print(len(name1))

s="Hello"

print(s*3) # This will print the string "Hello" three times.

print(name.capitalize()) # This will capitalize the first letter of the string and make all other letters lowercase.
print(name.upper()) # This will convert all the letters in the string to uppercase.
print(name.lower()) # This will convert all the letters in the string to lowercase.
print(name.replace("i", "y")) # This will replace all occurrences of "i" with "y" in the string. 

print(list(s)) # This will convert the string "Hello" into a list of characters. The output will be ['H', 'e', 'l', 'l', 'o'] 

name2="   Nitish Maurya   "
name2=name2.strip() # This will remove the leading and trailing whitespace from the string. The output will be "Nitish Maurya"
print(name2)

s1="--------------Hello World--------------"
s1=s1.strip("-") # This will remove the leading and trailing hyphens from the string. The output will be "Hello World"
print(s1)

s3="Hello my name is nitish and I am a software developer."
print(list(s3)) # This will convert the string into a list of characters. The output will be ['H', 'e', 'l', 'l', 'o', ' ', 'm', 'y', 
# ' ', 'n', 'a', 'm', 'e', ' ', 'i', 's', ' ', 'n', 'i', 't', 'i', 's', 'h', ' ', 'a', 'n', 'd', ' ', 'I', 
# ' ', 'a', 'm', ' ', 'a', ' ', 's', 'o', 'f', 't', 'w', 'a', 'r', 'e', ' ', 'd', 'e', 'v', 'e', 'l',
# 'o', 'p', 'e', 'r', 'd', 'e', 'v', 'e', 'l', 'o', 'p', 'e', 'r', '.']

print(s3.split(" ")) # This will split the string into a list of words using space as the delimiter.
# The output will be ['Hello', 'my', 'name', 'is', 'nitish', 'and', 'I', 'am', 'a', 'software', 'developer.']

print(s3.split("a")) # This will split the string into a list of substrings using "a" as the delimiter.
# The output will be ['Hello my n', 'me is nitish ', 'nd I ', 'm ', ' softw', 're developer.']

list=['h', 'e', 'l', 'l', 'o']
s4="".join(list) # This will join the list of characters into a string. The output will be "hello"
print(s4)

s5=" ".join(list) # This will join the list of characters into a string with a space as the delimiter. The output will be "h e l l o"
print(s5)

s6="-".join(list) # This will join the list of characters into a string with a hyphen as the delimiter. The output will be "h-e-l-l-o"
print(s6)