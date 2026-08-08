"""

Write a program to calculate the grade of a student from his marks from the following scheme:
90 - 100 => Ex
80 - 90 => A
70 - 80 => B
60 - 70 => C
50 - 60 => D
<50 => F

"""


grade = int(input("Enter your grade : "))

if grade >= 90 :
    print ("Excilent")

elif grade >= 80 and grade < 90 :
    print ("A")
elif grade >= 70 and grade < 80 :
    print ("B")
elif grade >= 60 and grade < 70 :
    print ("C")
elif grade >= 50 and grade < 60 :
    print ("D")
elif grade < 50 :
    print ("fail")

