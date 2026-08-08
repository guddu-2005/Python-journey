# Write a program to find whether a given username contains less than 10 characters or not.



name = input("Enter your name : ")
n1 = name.replace(" ","")
no = len(n1)

if no > 10 :
    print ("It contail more than 10 characters")

else :
    print("It containss less than 10 character")