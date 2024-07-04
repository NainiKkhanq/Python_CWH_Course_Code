#________________ Practise Test Chap 4 List and Tuples _________________________

# Q1: Write a program to store seven fruits in a list entered by the user

# fruits=[] 
# f1 = input("Enter First Fruit Name: ") 
# fruits.append(f1) 
# f2 = input("Enter Second Fruit Name: ") 
# fruits.append(f2) 
# f3 = input("Enter Three Fruit Name: ") 
# fruits.append(f3) 
# f4 = input("Enter Fourth Fruit Name: ") 
# fruits.append(f4) 
# f5 = input("Enter Fiveth Fruit Name: ") 
# fruits.append(f5) 
# f6 = input("Enter Sixth Fruit Name: ") 
# fruits.append(f6) 
# f7 = input("Enter Seventh Fruit Name: ") 
# fruits.append(f7) 
# f8 = input("Enter Eighth Fruit Name: ") 
# fruits.append(f8) 

# print(fruits[0:])

# Q2: Write a program to accept marks of 6 students and display them in a sorted manner

# stdMarks = []
# M1 = input("Enter First Subjects Marks: ")
# stdMarks.append(M1)
# M2 = input("Enter First Subjects Marks: ")
# stdMarks.append(M2)
# M1 = input("Enter First Subjects Marks: ")
# stdMarks.append(M1)
# M1 = input("Enter First Subjects Marks: ")
# stdMarks.append(M1)
# M1 = input("Enter First Subjects Marks: ")
# stdMarks.append(M1)
# M1 = input("Enter First Subjects Marks: ")
# stdMarks.append(M1)

# # Sorting the List
# stdMarks.sort() # Sort() method used for sorting
# print(stdMarks)

# Q3: Check that a tuple type cannot be changed in python

# a  =(10,10,32)
# a[0] = 10 # This will give error because Tuples is Immutable
# print(a)

# Q4: Write a program to sum a list with 4 numbers.

# a = [2,2,2,2]
# print([a[0]+a[1]+a[2]+a[3]])

# Q5: Write a program to count the number of zeros in the following tuple: Tuple is a = (7, 0, 8, 0, 0, 9)

a = (7, 0, 8, 0, 0, 9)
x = a.count(0) #Count will check how many times zero exists in this Tuple
print(x)
