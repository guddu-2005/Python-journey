'''
 Write a program to print the following star pattern.
*
***
***** for n = 3

'''


n = int(input("Enter your number : "))

for i in range (1, n+1) :
    p = "*"*(2 * i - 1)
    print(p)