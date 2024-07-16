# 6 Write a program to calculate the grade of a student from his marks from the
# following scheme:
# 90 – 100 => Ex
# 80 – 90 => A
# 70 – 80 => B
# 60 – 70 =>C
# 50 – 60 => D
# <50 => F


# Solution:
marks  = int(input("Enter Your marks: "))

if(marks <= 100 and marks >=90):
    print("Your Grade is EX")
elif(marks <90 and marks >=80):
    print("Your Grade is A")
elif(marks <80 and marks >=80):
    print("Your Grade is B")
elif(marks <70 and marks >=60):
    print("Your Grade is C")
elif(marks <60 and marks >=50):
    print("Your Grade is D")
elif(marks <50):
    print("You are Failed Grade F")



