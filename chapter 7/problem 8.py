'''

Write a program to print the following star pattern:
*
**
*** for n = 3

'''


n = int(input("Enter your number : "))

for i in range (1, n+2) :
    print ('*' * (1*i-1))