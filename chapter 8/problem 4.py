#  Write a recursive function to calculate the sum of first n natural numbers.



def sum (n) :
    add = 0
    for i in range (1, n + 1) :
        add = i + add
        
    print (add)

b = int (input ('Enter your number : '))    

sum (b)

