import pyttsx3
import os
#Q2: Use External module and Perform function of your interest

# Using pyttsx3 module (It will convert the text to speech in python).


engine = pyttsx3.init()
engine.say("Hello World How are You!")
engine.runAndWait()