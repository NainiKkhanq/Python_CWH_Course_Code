import pyttsx3
import os
# TO Print Multiple Lines under one Print Command Use Tripple Quotes

#Q1: Write a Poem using Print?
print('''Twinkle Twinkle, Little Star
How I wonder what you are
Up above the world so high
Like a diamond in the sky
Twinkle Twinkle Little Star
How I wonder what you are!
Twinkle Twinkle, Little Star
How I wonder what you are
Up above the world so high
Like a diamond in the sky
Twinkle Twinkle Little Star
How I wonder what you are!''')

#Q2: Use External module and Perform function of your interest

# Using pyttsx3 module (It will convert the text to speech in python).


engine = pyttsx3.init()
engine.say("Hello World How are You!")
engine.runAndWait()

#Q3:Write a python program to print the contents of a directory using the os module.
# Search online for the function which does that. 

# Get the directory path (replace 'path/to/your/directory' with your actual path)
directory_path = "/"

# Use os.listdir() to get a list of files and directories
contents = os.listdir(directory_path)

# Print the contents
print("Contents of", directory_path)
for item in contents:
  print(item)


