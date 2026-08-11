# Write a program to print multiplication table of n using for loops in reversed order.

n = int(input('Enter your number : ' ))

for i in range (10, -1, -1) :

    print (n, 'X', i, '=', i*n)