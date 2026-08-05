# Create an empty dictionary. Allow 4 friends to enter their favorite language as value and use key as their names. Assume that the names are unique.



d = {}

f1 = (input("Enter your 1st friend name : "))
f2 = (input("Enter your 2nd friend name : "))
f3 = (input("Enter your 3rd friend name : "))
f4 = (input("Enter your 4th friend name : "))


v1 = input("Enter your 1st friend favorite language : ")
v2 = input("Enter your 2nd friend favorite language : ")
v3 = input("Enter your 3rd friend favorite language : ")
v4 = input("Enter your 4th friend favorite language : ")


d.update ({f1:v1, f2:v2, f3:v3, f4:v4})

print (d)

