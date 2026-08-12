#  Write a program using functions to find greatest of three numbers.


def great () :
    a = int(input("Enter 1st number : "))
    b = int(input("Enter 2nd number : "))
    c = int(input("Enter 3rd number : "))

    if a > b :
        greater = a
    elif b > c :
        greater = b
    elif c > a :
        greater = c

    print ('Greatest no. is ',greater)

great()