#  Write a python function to print multiplication table of a given number.


def table (n):
    for i in range (0, 11):
        print (n, 'X', i, '=', i*n)

n = int (input ('Enter your digit : '))

table (n)