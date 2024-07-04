#___Practise Test of Strings Chap 3

#1: Write a python program to display a user entered name followed by Good Afternoon using input () function.

name = input("Please Enter Your Name: ")

print("Good After Noon" , name)

#2: Write a program to fill in a letter template given below with name and date.
# letter = '''
# Dear <|Name|>,
# You are selected!
# <|Date|>
# '''

letter  = f"Acceptance Letter! \n Dear {name} You are selected! \n 01/07/2024"

print(letter)

#3: Write a program to detect double space in a string.

subtitle = "Hello  How are you"
print(subtitle)
print(subtitle.__contains__("  "))
#4: Replace the double space from problem 3 with single spaces.
print(subtitle.replace("  "," "))
#5: Write a program to format the following letter using escape sequence characters.
# letter = "Dear Harry, this python course is nice. Thanks!"

letter = "Dear Harry,\nThis python course is nice.\nThanks!"
print(letter)
