# ******Arithmetic Operators*********

# +,-,*,/ are Arithmetic Operators

a = 10
b = 8
c = a+b
print(a+b)

# ****Assignment Operators******

x = 10
y  = x # we are assigning the x value in y
print(y)
# Increment operator  
g =10
g +=2 # Increase 2 more in g variable value and than again assign it to g
print(g)
g -=4 # Decrement 4 from g variable and again assign new vlaue to g
print(g)
g *=2 # Multiply the value of g variable with 2 and assign new value to g
print (g)
g /=2 # Divide the g variable value with 2 and again assign new value to g


# **** Comparison Operator ***** (They always return boolean (True  or False))

d = 5<4 # 5  is not less than 4 so it will return false and then it will save it in d variabel
print(d)

d= 5!=2 # It will return true because 5 is not equal to 2
print (d) 

d = 5<=1 # it will return false because 5 is not less than 1 its greater than 1
print(d)

#******** Logical Operators ************

# ** Refer to Truth Table of Logical Operators for Better Understanding.****

e = True or False # In OR Operator logic if One value is True it will return True
print(e)

e = True and False # If both values are true then AND Operator will give True otherwise it will return false
print (e)


print (not(True)) # Not Operator always convert the True to False and False to True
