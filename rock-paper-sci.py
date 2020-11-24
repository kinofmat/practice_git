from random import randint

print("Welcome to this game of Rock, Paper, Scissors!\n")

t = ["Rock", "Paper", "Scissors"]
computer = t[randint(0,2)]

again = "y"
count = 0

while again == "y" or again == "Y":
    value = input("Please enter 'Rock', 'Paper', or 'Scissors' ")
    if value == computer:
        print("Tie!")
    elif value == "Rock":
        if computer == "Paper":
            print("Sorry, you lost!", computer, "covers", value)
        else:
            print("You win!", value, "smashes", computer)
    elif value == "Paper":
        if computer == "Scissors":
            print("Sorry, you lost!", computer, "cut", value)
        else:
            print("Congrats, you won!", value, "covers", computer)
    elif value == "Scissors":
        if computer == "Rock":
            print("You lost!", computer, "smashes", value)
        else:
            print("Congrats, you won!", value, "cut", computer)
    else:
        print("I cannot understand. Maybe check your spelling.")
    count += 1
    print(count)
    if count%3 == 0:
        again = input("Do you want to play again? (y/n) ")
    computer = t[randint(0,2)]