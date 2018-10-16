from random import randint

# Initialise variables
game = True
player = True

print("Welcome to a game of rock, paper, scissors.\n")

while game == True:
    playerchoice = input("Choose rock (r), paper (p) or scissors (s), or q to quit: \n")
    computer = randint(0,2)
    if playerchoice == 'q':
        game == False
        break
    elif playerchoice == 'r':
        player = 0
    elif playerchoice == 'p':
        player = 1
    elif playerchoice == 's':
        player = 2
    else:
        playerchoice = input("Wrong type of input. Please try again: \n")

    if player == computer:
        print("It's a tie!\n")
    elif player == 0:
        if computer == 1:
            print("Paper beats rock. Computer wins.\n")
        elif computer == 2:
            print("Rock beats scissors. Player wins.\n")
    elif player == 1:
        if computer == 2:
            print("Scissors beat paper. Computer wins.\n")
        elif computer == 0:
            print("Paper beats rock. Player wins.\n")
    elif player == 2:
        if computer == 0:
            print("Rock beats scissors. Computer wins.\n")
        elif computer == 1:
            print("Scissors beat paper. Player wins.\n")
