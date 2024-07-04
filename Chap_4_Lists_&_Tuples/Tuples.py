#_____________________ TUPLES _____________IN PYTHON_____________

# TUPLES are immutable.

a= (1,2,3,4,5)
print(type(a)) # Returning the class name so its tuple

a = () # its a Empty Tuple
# Storing Single value in Tuple so to do this we will use value and than comma then it will take it as tuple
a = (1,) #now Python will considered this as tuple because we use comma which means we will add more values

b = (1,3,4,False,"Rohan","Shivam") # You can add values in tuples with different Data Types
print(b)

#____Changing Tuples Value_______
# b[0] = 10 # This will return error because value of Tuples is not changeable its permanent,
# print(b)


#_____________METHOD OF TUPLES ___________________!

#Collection of Different values with differ datatypes

x = (12,14,12,16,"Hello","Python",True, False, 220.1) 

#1 Count() Method. This Method will check how many time entered value exists in Tuples For Example

no = x.count(12) # in x tuple 12 is available only two times so it will return 2
print(no)
no = x.count("Python") # Similarly you can check it the string value how many time Python word exists
print (no)  # It will return 1 because Python exists only one time in a Tuple

#2 index() This method will return the index number of the entered value 
y = x.index(16) # 16 number in tuple is on 3rd Index so it will return 3 which means 16 value is on 3rd index
print(y)

#  Membership it will tell us is entered value exists or not if not it will return False or true in other case

print(12 in x) # So 12 exists in x Tuple so it will return True 
print(234 in x) # It will return False because 234 value does not exists in Tuple

# Check total length of tuple len()
print(len(x))

#Slicing, in Tuples 
y = x[0:4] # It will print the value from 0 index to 4 Index 
print(y)