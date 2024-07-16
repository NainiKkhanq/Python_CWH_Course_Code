#   3: A spam comment is defined as a text containing following keywords:
# “Make a lot of money”, “buy now”, “subscribe this”, “click this”. Write a program
# to detect these spams.

c1 = "buy now"
c2 = "subscribe this"
c3 = "click this"
c4 = "Make a lot of money"
comment = input("Enter Comment: ")

if((c1 in comment) or (c2 in comment) or (c3 in comment) or (c4 in comment)):
    print("Spam Detected Comment Removed by Owner")
else:
    print("Comment Posted!")