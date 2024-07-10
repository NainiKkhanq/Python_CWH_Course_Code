#We also Use Dictionaries to save collection of data
# We save values in Dictionary in the form of key and values

# IN Below example marks is a dictionary and in it 'Dart' is the key and it has a value of 100

marks = {

    'Dart':100,
    'Java': 20,
    'Python': 10
}

#Check the type of marks{} 
print(type(marks))
# printing dictionary
print(marks)
# Printing one single key from the dictionary so we can't use [0] index like this
# We will simply call the Key name to get that value

print(marks['Dart'])

#_________METHODS IN DICTIONARY_________________
#1: .item() this method give us the result in the form of tuples
print(marks.items())

#2: keys() this method give us the only keys of dictionary
print(marks.keys())

#3 values() This method will just print the values of Marks Dictionary
print(marks.values())

#4 Updating the Dictionary so we will enter the Key and also we will enter the new value
marks.update({"Dart":99}) #Similarly Like distionary we will call the Key in Curly Brackets and assign the value in it 
print(marks) # Now the original dictionary will be updated the reason is Dictionary is Mutable
# Jo Key dictionary ka andr hogi aus ki value update hogi or jo nhi hogi aus ki new key or value bna dy ga
#5 Adding new Key and Value so to add new key and value in dictionary we will use the same method if Ruby is not in dictionary so it will ad it
marks.update({"Ruby":7829})
print(marks)  # So ruby is now added as a key and 7829 is a value of Rubys

#6 Get the  value of specific key using this get() method
print(marks.get("Dart")) # This wil specifically retured the value of Dart key
#print(marks['Dart']) and marks.get("Dart") # Both will works same but  the point is if the key not exists in dictionary
# In that case ['Dart'] this will return error but the .get("Dart") this will return None.

#7 clear Method this will remove all Keys and values from the Dictionary

# marks.clear()
# print(marks)

# remove singel key and its value form Dictionary
marks.pop('Dart')#
print(marks)


