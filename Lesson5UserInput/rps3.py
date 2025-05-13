import sys #To use sys.exit
import random
from enum import Enum #we only want enum from that module

# Shift + Tab makes the backword tab
# In rps 3 we deleted while and replace with recursion
# Adding functions
def play_rps(): #Newly added line for rps3
    class RPS(Enum):
        ROCK = 1 #Naming is to use all capital when used Enums
        PAPER = 2
        SISSOR = 3

    playerchoice = input("\nEnter... \n1 for Rock,\n2 For Paper, or \n3 For Sissor:\n\n")

    #Added new in rps 3
    if playerchoice not in ["1", "2", "3"]:
        print("You must enter 1, 2 or 3")
        return play_rps() # recursion

    player = int(playerchoice) #Playerchoice cannot be compared because it was string so we need to typecast to int

    computerchoice = random.choice("123") #will choose 1 2 3 but it is string, so we need to cast that to int

    computer = int(computerchoice)

    print("You chose " + str(RPS(player)).replace('RPS.', '') +".") #Change number to Rock paper sissor, replace RPS Because it is showing in the code.
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

    print("\nPlay again?") # Added new in rps3

    while True: # Added new in rps3
        playagain = input("\nPlay again? \nY for Yes or \nQ to Quit \n\n")
        if playagain.lower() not in ["y", "q"]:
            continue # if the input is not y or q it is gonna loop again and ask for the y or q again
        else:
            break

    if playagain.lower() == "y": #This changes the input to change lowercase to check easier.
        return play_rps() # Added the reculsive function, it is a good place to add because they want to play again
    else:
        print("Thanks for playing!")
        sys.exit("Bye! 👋")
        # break We could use this too 

play_rps()