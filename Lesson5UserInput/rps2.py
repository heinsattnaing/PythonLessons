import sys #To use sys.exit
import random
from enum import Enum #we only want enum from that module

class RPS(Enum):
    ROCK = 1 #Naming is TO use all capital when used Enums
    PAPER = 2
    SISSOR = 3

playagain = True

while playagain: #Make sure when used while code in python below if while loop want to affect need to be tabed
    playerchoice = input("\nEnter... \n1 for Rock,\n2 For Paper, or \n3 For Sissor:\n\n")

    player = int(playerchoice) #Playerchoice cannot be compared because it was string so we need to typecast to int
    
    if player < 1 or player > 3:
        sys.exit("You must enter 1, 2 or 3.") #This will exit the program but will still give message to the user

    computerchoice = random.choice("123") #will choose 1 2 3 but it is string, so we need to cast that to int

    computer = int(computerchoice)

    print("/nYou chose " + str(RPS(player)).replace('RPS.', '') +".") #Change number to Rock paper sissor, replace RPS Because it is showing in the code.
    print("Computer chose " + str(RPS(computer)).replace('RPS.', '') +".\n")

    if player == 1 and computer == 3: #Window + , to use emojis
        print("You Win!✌")
    elif player == 2 and computer == 1:
        print("You Win!✌")
    elif player == 3 and computer == 2:
        print("You Win!✌")
    elif player == computer:
        print("Draw!")
    else: 
        print("Computer Wins!😂")

    playagain = input("\nPlay again? \nY for Yes or \nQ to Quit \n\n")

    if playagain.lower() == "y": #This changes the input to change lowercase to check easier.
        continue
    else:
        print("Thanks for playing!")
        playagain = False
        # break We could use this too 
sys.exit("Bye! 👋")