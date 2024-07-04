# Check the Class of Variable either its Integer, String , Boolean or Float or Double To check this

a  =10
print(type(a)) # We know a is integer type variable but still we can check it using type() method in Python


a  ="Hello Word"
print(type(a)) # Now in this case we stored String in a variable so the type will also be String

a = True
print(type(a)) # Type of a is now Boolean so it will print the Type of a is Boolean


# Type Casting in Python Now we will Change the int to String, String to Int, float to int like this but with valid rules

# Converting String to Float so i will do it like this

e = "12.3" # it's a String value

b = float(e) # Now with the help of float i will convert the string value to float

print (type(b)) # Checking  the type is change or not so it's change

# int to String conversion

x = 1402
y = str(x) # str(value) this will convert the x int value into string 
print(type(y))
