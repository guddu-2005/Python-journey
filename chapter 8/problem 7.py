#  Write a python function to remove a given word from a list and strip it at the same time.


def remove (c) :
    l = []
    for word in a :
        word = word.strip()

        if word.lower() != c.lower():
            l.append(word)
    print (l)


a = ["Harry", "  Soham", "Sachin  ", "  Rahul  "]

print (a)

name = input("Enter a name to remove from the above list : ")

remove(name)