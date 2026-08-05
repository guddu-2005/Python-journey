# Write a program to input eight numbers from the user and display all the unique numbers (once).



s = set()


l1 = int(input("Enter your 1st number : "))
l2 = int(input("Enter your 2nd number : "))
l3 = int(input("Enter your 3rd number : "))
l4 = int(input("Enter your 4th number : "))
l5 = int(input("Enter your 5th number : "))
l6 = int(input("Enter your 6th number : "))
l7 = int(input("Enter your 7th number : "))
l8 = int(input("Enter your 8th number : "))


s1 = s.union({l1,l2,l3,l4,l5,l6,l7,l8})

print (s1)