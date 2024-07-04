#1 Adding two Numbers

a  =10
b =20
print(a+b)

#2 Write a python program to find remainder when a number is divided by z.

x  =37
y  =5
print('Remainder is: ', x % y) # % is a moduolo operator we use this method to get remainders


#3 Check the type of variable assigned using input () function.

z = input("Enter value to check its Type: ")
print("The type of entered value is: ",type(z))

#4 Use comparison operator to find out whether ‘a’ given variable a is greater than
# ‘b’ or not. Take a = 34 and b = 80

u = 34
t = 80
print(u >t)


#5  Write a python program to find an average of two numbers entered by the user.

firstNumber = int(input("Enter First Number: ") )
secondNumber = int(input("Enter Second Number: ") )
sum = (firstNumber + secondNumber) / 2
print(sum)

#6 Write a python program to calculate the square of a number entered by the user

enteredNumber = int(input("Enter Number to Find Square: "))

result = enteredNumber **2 # use this way to get square value (**2, **4 **10)
print(result)
