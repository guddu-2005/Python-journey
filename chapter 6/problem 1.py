#  Write a program to find the greatest of four numbers entered by the user.



a = int(input("Enter 1st number : "))
b = int(input("Enter 2nd number : "))
c = int(input("Enter 3rd number : "))
d = int(input("Enter 4th number : "))


# if a>b and a>c and a>d :
#     print("a is greater")
# if b>a and b>c and b>d :
#     print("b is greater")
# if c>a and c>b and c>d :
#     print("c is greater")
# if d>a and d>b and d>c :
#     print("d is greater")






greatest = a 

if b > greatest :
    greatest = b

if c > greatest:
    greatest = c

if d > greatest:
    greatest = d



print("The greatest value is : ",greatest)
    