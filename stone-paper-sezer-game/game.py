import random
dict = {"stone" : 1, "paper" : 0, "sezer" : -1}
reversedict = {1 : "stone", 0 : "paper", -1 : "sezer"}
computer = random.choice([-1, 0, 1])

enter = input("Enter your choice (stone, paper, sezer) : ")

you = dict[enter] 
'''
stone = 1
paper = 0
sezer = -1

computer = 1 / you = 0 => me = 1 
computer = 1 / you = -1 => com = 2
computer = 0 / you = 1 => com = -1
computer = 0 / you = -1 => me = 1
computer = -1 / you = 1 => me = -2
computer = -1 / you = 0 => com = -1

me = 1, -2
computer = 2, -1
'''

if computer == you:
    print("Draw!")

else:
    if computer - you == 1 or computer - you == -2:
        print ("You win")  
        print (f"You chose {reversedict[you]}, computer chose {reversedict[computer]}")

    else:
        print("You lose, computer win")
        print (f"You chose {reversedict[you]}, computer chose {reversedict[computer]}")