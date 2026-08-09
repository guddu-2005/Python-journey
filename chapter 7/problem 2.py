"""Write a program to greet all the person names stored in a list 'l' and which starts with S.
l = ["Harry", "Soham", "Sachin", "Rahul"]"""




l = ["Harry", "Soham", "Sachin", "Rahul"]

# i = 0 

# while i < len(l) :
#     if l[i].startswith("S") :
#         print (f"Hello {l[i]}")

#     i = i + 1


for word in l:
    
    if word.startswith ("S"):
        print (f"Hello {word}")