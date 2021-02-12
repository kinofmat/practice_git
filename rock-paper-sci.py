from random import randint # Library for random numbers.

print("Welcome to this game of Rock, Paper, Scissors!\n") # Initial welcome when first time loading screen.

t = ["Rock", "Paper", "Scissors"]
computer = t[randint(0,2)] # Creates a random integer from the values 0-2 inclusive.

again = "y"
count = 0
w = 0
l = 0

while again == "y" or again == "Y":
    value = input("Please enter 'Rock', 'Paper', or 'Scissors' ")
    if value == computer:
        print("Tie!")
    elif value == "Rock":
        if computer == "Paper":
            print("Sorry, you lost!", computer, "covers", value)
            l += 1
        else:
            print("You win!", value, "smashes", computer)
            w += 1
    elif value == "Paper":
        if computer == "Scissors":
            print("Sorry! you lost!", computer, "cut", value)
            l += 1
        else:
            print("Congrats, you won!", value, "covers", computer)
            w += 1
    elif value == "Scissors":
        if computer == "Rock":
            print("You lost!", computer, "smashes", value)
            l += 1
        else:
            print("Congrats! you won!", value, "cut", computer)
            w += 1
    else:
        print("I cannot understand. Maybe check your spelling.")
    count += 1
    if count%3 == 0:
        if w > 1:
            print("You won a total of {} times and lost {} time." .format(w, l))
        elif l > 1:
            print("You won {} time and lost {} times." .format(w, l))
        elif w < 2 and l < 2:
            print("You won {} time and lost {} time." .format(w, l))
        elif w < 1 and l < 1:
            print("You won a total of {} times and lost {} times." .format(w, l))
        elif w == 3:
            print("Wow, what a show! You won every time!")
        elif l == 3:
            print("You didn't win any time. That's too bad. Maybe try again?")
        again = input("Do you want to play again? (y/n) ")
        if again == y:
            w = 0
            l = 0
    computer = t[randint(0,2)]