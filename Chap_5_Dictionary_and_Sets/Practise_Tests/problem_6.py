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
