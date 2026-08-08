#  Write a program which finds out whether a given name is present in a list or not.


list = ["raj","saan","guddu","bibhu","sonu","rihan","sai"]


name = input("Enter your name : ")

name = name.lower()

if name in list :
    print ("Your name in list")

else :
    print ("Your name is not in list")