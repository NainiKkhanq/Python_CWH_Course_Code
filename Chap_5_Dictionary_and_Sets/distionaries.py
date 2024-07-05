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