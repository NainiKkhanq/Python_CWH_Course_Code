# 7. Write a program to find out whether a given post is talking about “Harry” or not.

post = input("Type Your Post: ")
a = "Harry"
# .lower() will convert the text to lower case and than check the condition
if(a.lower() in post.lower()):
    print("Harry Found")
else:
    print("Harry Not Found")


