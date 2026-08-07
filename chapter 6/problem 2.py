'''Write a program to find out whether a student has passed or failed if it requires a total of 40% and at least 33% in each subject to pass. Assume 3 subjects and take marks as an input from the user.'''






sub1 = int(input("Enter 1st subject mark : "))
sub2 = int(input("Enter 2nd subject mark : "))
sub3 = int(input("Enter 3rd subject mark : "))

avg = (sub1+sub2+sub3)/3

if sub1 > 33 and sub2 > 33 and sub3 > 33 and avg > 40 :
    print ("Pass the exam")

else :
    print ("fail the exam")