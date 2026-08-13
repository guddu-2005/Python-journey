'''

Write a python function to print first n lines of the following pattern.

***
**
*
 
for n = 3

'''



def star (n) :
    for i in range (n , 0, -1) :
        print ('*' * i)

n = 3

star (n)