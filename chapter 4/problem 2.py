# Write a program to accept marks of 6 students and display them in a sorted manner.



marks = []

m1 = int (input("Enter marks of 1st student : "))
m2 = int (input("Enter marks of 2nd student : "))
m3 = int (input("Enter marks of 3rd student : "))
m4 = int (input("Enter marks of 4th student : "))
m5 = int (input("Enter marks of 5th student : "))
m6 = int (input("Enter marks of 6th student : "))


marks.extend([m1,m2,m3,m4,m5,m6])

marks.sort()

print (marks)