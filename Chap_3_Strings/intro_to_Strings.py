#There are many Differen Ways to make String in Python

name = "Hello" # its a String

# Others methods to make strings are

# You can write Strings in single line quotes, Multi Line quotes and than in trippple lines quote
# For Example

name = 'Hello' #Single Quote
name = "Hello" #Double Quote
#name = '''Hello Buddy''' # Tripple Quotes

# String Slicing....
# String is Immutable (Once String is created you can't change it but you can create a new one)
# Hello is a String you can't change the H and o from that string but you can create new one

# ** Indexing in String ** 
# In every programming we have Indexing so in String we have index and on index we have values
# Like H E L L O [0,1,2,3,4] on 0 Index we have H and on 1 index we have E so String created like this

# Similary when we start indexing from left to right we count it from 0 index but
# When we start it from end we sart indexing from -1, -2 like this.

#******** Getting Some alphabets from strings like this use variable name put array brackets []
# and then enter the start and end index (Jahan sa ly kr jahan tk ap string ko slice krna chahty vo index likhan ha)
print(name [0:3]) # Start from Index 0 to index 3 and it will print all words from index 0 to 3

#*** Getting single Chracter from String... To do this***

print (name[1]) # Form first index it will print the character


# *** Negative Slicing of String (It will start indexing from end)

print(name[-5:-2]) # Indexing will be start from the End of String

print(name[0:]) # It will start printing the string from 0 index to till the whole length
print(name[:4]) # It will start printing the string from 0 index to till 4 index

# numbers = "123456789"
# print(numbers[1:7:3])


