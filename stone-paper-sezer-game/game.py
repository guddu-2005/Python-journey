import random
dict = {"stone" : 1, "paper" : 0, "sezer" : -1}
reversedict = {1 : "stone", 0 : "paper", -1 : "sezer"}



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
            
