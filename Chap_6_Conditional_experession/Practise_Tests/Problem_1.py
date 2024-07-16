#1 Write a program to find the greatest of four numbers entered by the user

a1 = int(input("Enter Num 1: "))
a2 = int(input("Enter Num 2: "))
a3 = int(input("Enter Num 3: "))
a4 = int(input("Enter Num 4: "))

if(a1 > a2 and a1 >a3 and a1>a4):
    print(a1, "Is the Greatest Number")
elif(a2>a1 and a2>a3 and a2>a4):
    print(a2, "Is the Greatest Number")
elif(a3>a1 and a3 >a2 and a3>a4):
    print(a3, "Is the Greatest Number")
elif(a4>a1 and a4>a2 and a4>a3):
    print(a4,"Is the Greatest Number")
else:
    print("All Numbers are Equal")
