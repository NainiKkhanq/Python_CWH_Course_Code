

# Write a program to input eight numbers from the user and display all the unique numbers (once).
s =set() # Write set when you create empty set

n  = input('Enter Number: ')

s.add((int(n)))
n  = input('Enter Number: ')

s.add((int(n)))
n  = input('Enter Number: ')

s.add((int(n)))


print(s)