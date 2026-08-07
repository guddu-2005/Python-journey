"""A spam comment is defined as a text containing following keywords: “Make a lot of money”, “buy now”, “subscribe this”, “click this”. Write a program to detect these spams.
"""



text = input("Enter the text : ")

lib = [
    'make a lot of money',
    'buy now',
    'subscribe this',
    'click this',
]


if lib in text :
    print ("This message is spam")

else :
    print ("It is not a spam")