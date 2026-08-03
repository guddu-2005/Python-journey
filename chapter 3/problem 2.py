"""
Write a program to fill in a letter template given below with name and date.
letter = '''
Dear <|Name|>,
You are selected!
<|Date|>
'''
"""

from datetime import date

today = date.today()

letter = "Dear name\nYou are selected.\ndate"

name = input("Enter your name : ")

fletter = letter.replace("name", name)
fletter = fletter.replace("date", str(today))

# print (fletter)

# print("Dear", name, "\nYou are selected\n", today)

print(f"Dear {name}\n You are selected\n {today}")