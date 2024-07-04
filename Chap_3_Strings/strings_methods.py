#___ Strings Method ____

#1: ____ Get Length of String ___ 
name = "Naini"

print(len(name))

#2: _____ check the ending of the String __It will return True/False___
print(name.endswith("i"))

#3: _____check the starting of the String __It will return True/False___

print(name.startswith('N'))

#4:_____make the String First letter Capital__It will return Capital the first Letter of Strings___

print(name.capitalize())

#5:___strip()__ Removes leading and trailing whitespace___
print(name.strip()) 

#6:___replace()__Replaces all occurrences of a substring with another substring.___
print(name.replace("N","T"))
 
#7:___upper()__Converts all characters to uppercase. Similary we have lower()___
print(name.upper())

#8:___find()____Find the first (or last) occurrence of a substring and return its index
story = "Once upon a time there is a boy called Tony"
print(story.find("Tony"))

