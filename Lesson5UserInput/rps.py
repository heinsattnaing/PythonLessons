import sys #To use sys.exit
import random
from enum import Enum #we only want enum from that module

class RPS(Enum):
    ROCK = 1 #Naming is TO use all capital when used Enums
    PAPER = 2
    SISSOR = 3

print("") #To Know the another game is happening after the one game finished
playerchoice = input("Enter... \n1 for Rock,\n2 For Paper, or \n3 For Sissor:\n\n")

player = int(playerchoice) #Playerchoice cannot be compared because it was string so we need to typecast to int
 
if player < 1 or player > 3:
    sys.exit("You must enter 1, 2 or 3.") #This will exit the program but will still give message to the user

computerchoice = random.choice("123") #will choose 1 2 3 but it is string, so we need to cast that to int

computer = int(computerchoice)

print("")
print("You chose " + str(RPS(player)).replace('RPS.', '') +".") #Change number to Rock paper sissor, replace RPS Because it is showing in the code.
print("Computer chose " + str(RPS(computer)).replace('RPS.', '') +".")
print("")

if player == 1 and computer == 3:
    print("You Win!✌")
elif player == 2 and computer == 1:
    print("You Win!")
elif player == 3 and computer == 2:
    print("You Win!")
elif player == computer:
    print("Draw!")
else: 
    print("Computer Wins!😂")
    