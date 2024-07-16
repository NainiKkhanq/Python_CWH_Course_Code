#2: Write a program to find out whether a student has passed or failed if it requires a
# total of 40% and at least 33% in each subject to pass. Assume 3 subjects and
# take marks as an input from the user


marks1 = int(input("Enter Subject 1 Marks: "))
marks2 = int(input("Enter Subject 2 Marks: "))
marks3 = int(input("Enter Subject 3 Marks: "))

total_percentage = (100*(marks1 + marks2 + marks3))/300

if(marks1 and marks2 and marks3 <= 100):
    if(total_percentage >=33 and marks1>=33 and marks2>=33 and marks3>33):
        print("Good Job You got ", total_percentage," And You Passed the Exam")
    else:
       print("Better Luck Next Time ", total_percentage," And You failed in Exam")
else:
    print("Invalid marks ")