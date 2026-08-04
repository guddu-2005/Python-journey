# Write a program to sum a list with 4 numbers.




list = []

l1 = int(input("Enter 1st number : "))
l2 = int(input("Enter 2nd number : "))
l3 = int(input("Enter 3rd number : "))
l4 = int(input("Enter 4th number : "))

list.extend([l1,l2,l3,l4])

sum = sum(list)

print("\nYou enterd ", list)

print ("\nSum of all no. : ",sum)