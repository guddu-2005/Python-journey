"""
Write a program to read the text from a given file ‘poems.txt’ and find out whether it
contains the word ‘twinkle’.
"""


with open ("chapter 9/poems.txt") as f :
    txt = f.read()

find = "twinkle"

if find in txt :
    print("This file contain the word \"twinkle\"")
else :
    print("This file does not contain the word \"twinkle\"")