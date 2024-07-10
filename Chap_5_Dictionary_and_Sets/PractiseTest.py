# Write a program to create a dictionary of Hindi words with values as their English
# translation. Provide user with an option to look it up

# dictionary =  {
# "Lets Go" : "Chaloo",
# "Cat" : "Billi",
# "Room" : "Kamra"



# }

# word = input("Enter The word to Get meaning: ")

# print(dictionary[word])
 

# Write a program to input eight numbers from the user and display all the unique numbers (once).
# s =set() # Write set when you create empty set

# n  = input('Enter Number: ')

# s.add((int(n)))
# n  = input('Enter Number: ')

# s.add((int(n)))
# n  = input('Enter Number: ')

# s.add((int(n)))


# print(s)



# 3. Can we have a set with 18 (int) and '18' (str) as a value in it?


# set = {1,2,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,"A","B","C","D","E","F","G","H","J","K","L","M","N","O","P","Q","R","T","U","V"}
# print(set)

# The Answer is True____!

# What will be the length of following set s:
# s = set()
# s.add(20)
# s.add(20.0)
# s.add('20') # length of s after these operations?

v = set()
v.add(20)
v.add(20.0)
v.add('20')
print(v.__len__())
# The length of this Set will be 

#5 s = {}
# What is the type of 's'?
s ={}
print(type(s)) # Type is Dictionary

#6: 6. Create an empty dictionary. Allow 4 friends to enter their favorite language as
# value and use key as their names. Assume that the names are unique

lang = {}
f1Name = input("Your Name: ")
f1Lang = input("Favorite Language: ")
lang.update({f1Name:f1Lang})
f2Name = input("Your Name: ")
f2Lang = input("Favorite Language: ")
lang.update({f2Name:f2Lang})
f3Name = input("Your Name: ")
f3Lang = input("Favorite Language: ")
lang.update({f3Name:f3Lang})
f4Name = input("Your Name: ")
f4Lang = input("Favorite Language: ")
lang.update({f4Name:f4Lang})

print(lang)

#7 If the names of 2 friends are same; what will happen to the program in problem 6?
# This will update the old User Data

#8 If languages of two friends are same; what will happen to the program in problem 6?
# Nothing will happend it will add the value as per its keys.

#9. Can you change the values inside a list which is contained in set S?
s = {8, 7, 12, "Harry", [1,2]}

# List inside set is not writeable and also its not changeable because set has no indexing