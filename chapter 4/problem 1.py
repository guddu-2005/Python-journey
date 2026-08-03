# Write a program to store seven fruits in a list entered by the user.


list = []

l1 = input ('Enter 1st fruit : ')
list.append(l1)

l2 = input ('Enter 2nd fruit : ')
list.append(l2)

# l3 = input ('Enter 3rd fruit : ')
# list.append(l3)

# l4 = input ('Enter 4th fruit : ')
# list.append(l4)

# l5 = input ('Enter 5th fruit : ')
# list.append(l5)

# l6 = input ('Enter 6th fruit : ')
# list.append(l6)

# l7 = input ('Enter 7th fruit : ')
# list.append(l7)

l8 = list.extend([l1,l2])

print (list)
