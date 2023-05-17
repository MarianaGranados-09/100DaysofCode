##rock paper scissors game

import random

def computerChoice():
    randnum = random.randint(1,3)
    if(randnum == 1):
        choiceC = "rock"
    elif(randnum == 2):
        choiceC = "paper"
    elif(randnum == 3):
        choiceC = "scissors"
    return choiceC   


choiceHuman = input("Choose rock, paper or scissors: ")
choiceComputer = computerChoice()
print(f"Computer chose {choiceComputer}")
if(choiceHuman == choiceComputer):
    print("It's a tie!")
elif(choiceHuman == 'rock' and choiceComputer == 'paper'):
    print("Computer wins!")
elif(choiceHuman == 'paper' and choiceComputer == 'rock'):
    print("Human wins!")
elif(choiceHuman == 'scissors' and choiceComputer == 'paper'):
    print("Human wins!")
elif(choiceHuman == 'paper' and choiceComputer == 'scissors'):
    print("Computer wins!")
elif(choiceHuman == 'rock' and choiceComputer == 'scissors'):
    print("Human wins!")
elif(choiceHuman == 'scissors' and choiceComputer == 'rock'):
    print("Computer wins!")
