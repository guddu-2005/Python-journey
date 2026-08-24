"""The game() function in a program lets a user play a game and returns the score as an
integer. You need to read a file ‘Hi-score.txt’ which is either blank or contains the previous
Hi-score. You need to write a program to update the Hi-score whenever the game()
function breaks the Hi-score.
"""

import random

def game (y, c) :
    if c - y == 1 or c - y == -2:
        with open ("high-score.txt",) as score :
            score = int(score.read())
            print (f"Previous score : {score}")
            score = score + 1

        with open ("high-score.txt", "w") as f :

            f.write(str(score))
            print (f"new score : {score}")

    else :
        with open ("high-score.txt",) as score :
            score = score.read()
            print (f"Previous score : {score}")
            print (f"new score : {score}")

            
dict = {"stone" : 1, "paper" : 0, "sezer" : -1}
reversedict = {1 : "stone", 0 : "paper", -1 : "sezer"}

while True :

    computer = random.choice([-1, 0, 1])
    print ("\n<============================>\n")
    enter = input("Enter your choice (stone, paper, sezer) : ")
    you = dict[enter] 

    if computer == you:
        print("\nDraw!\n")
        print (f"You chose {reversedict[you]}, computer chose {reversedict[computer]}\n")


    else:
        if computer - you == 1 or computer - you == -2:
            print ("\nYou win\n")  
            print (f"You chose {reversedict[you]}, computer chose {reversedict[computer]}\n")

        else:
            print("\nYou lose, computer win\n")
            print (f"You chose {reversedict[you]}, computer chose {reversedict[computer]}\n")
    
    game(you, computer)
