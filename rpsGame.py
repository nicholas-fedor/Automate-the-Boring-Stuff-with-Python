import random, sys

print("Welcome to the game: Rock, Paper, Scissors!")

# These variables keep track of the number of wins, losses, and ties.
wins = 0
losses = 0
ties = 0

while True: # The main game loop
    print("%s Wins, %s Losses, %s Ties" % (wins, losses, ties))
    while True: # Player input loop
        print("Enter your choice: (r)ock, (p)aper, (s)cissors or (q)uit")
        playerMove = input()
        if playerMove == "q":
            sys.exit() # Quits the program
        if playerMove == "r" or playerMove == "p" or playerMove  == "s":
            break # Break out of the player input loop.

    # Display what the player chose.
    if playerMove == "r":
        print("Rock versus...")
    elif playerMove == "p":
        print("Paper versus...")
    elif playerMove == "s":
        print("Scissors versus...")

    # Display the computer's move.
    randomNumber = random.randint(1,3)
    if randomNumber == 1:
        computerMove = "r"
        print("Rock")
    elif randomNumber == 2:
        computerMove = "p"
        print("Paper")
    elif randomNumber == 3:
        computerMove = "s"
        print("Scissors")

    # Display and record the win/loss/tie.
    if playerMove == computerMove:
        print("It is a tie!")
        ties = ties + 1
    elif playerMove == "r" and computerMove == "s":
        print("You win!")
        wins = wins + 1
    elif playerMove == "p" and computerMove == "r":
        print("You win!")
        wins = wins + 1
    elif playerMove == "s" and computerMove == "p":
        print("You win!")
        wins = wins + 1
    elif playerMove == "r" and computerMove == "p":
        print("Computer wins!")
        losses = losses + 1
    elif playerMove == "p" and computerMove == "s":
        print("Computer wins!")
        losses = losses + 1
    elif playerMove == "s" and computerMove == "r":
        print("Computer wins!")
        losses = losses + 1