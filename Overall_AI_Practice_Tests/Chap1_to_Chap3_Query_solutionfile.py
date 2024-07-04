

#1_____________Solution___________________

firstName = input("Enter First Name: ")
secondName = input("Enter Second Name: ")
fullName = firstName.upper()+ " " + secondName.upper()

print("Greeting: " + f"{fullName}" )


#2___________________Solution______________________
sentence = input("Enter Sentence: ")
print(f"Your Sentence Is: {sentence.upper()} and Your Sentence Total length is {len(sentence)}")


#3_____________Solution__________________

age = int(input("What is your Age: "))

if(age >= 18):
    print("Welcome Please cast your vote")
else:
    print("Sorry You are not able for Voting")
