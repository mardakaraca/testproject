import random
import itertools
from itertools import chain
def combination(string):
    result = map(''.join, itertools.product(*((c.lower(), c.upper()) for c in string)))
    return list(result)

while True:
    rock_list = (combination("rock"))
    paper_list = (combination("paper"))
    scissors_list = (combination("scissors"))
    big_choice_list = [rock_list, paper_list, scissors_list]
    flat_choice_list = list(chain.from_iterable(big_choice_list))
    user_choice = input("Choose Rock, Paper or Scissors: \nPress 'Q' to Exit The Game")
    if user_choice == "q" or user_choice == "Q":
        print("Exiting...")
        break

    elif user_choice not in flat_choice_list:
        print("Please Enter Correctly!")

    else:
        if user_choice in rock_list:
            user_choice = "Rock"

        elif user_choice in paper_list:
            user_choice = "Paper"

        elif user_choice in scissors_list:
            user_choice = "Scissors"
        choice_list = ["Rock", "Paper", "Scissors"]
        computer_choice = random.choice(choice_list)
        print(f"Computer's choice: {computer_choice}")

        if user_choice == computer_choice:
            print("Draw")

        elif ((user_choice == "Rock" and computer_choice == "Scissors") or
            (user_choice == "Paper" and computer_choice == "Rock") or
            (user_choice == "Scissors" and computer_choice == "Paper")):
            print("YOU WIN!")

        elif ((user_choice == "Rock" and computer_choice == "Paper") or
            (user_choice == "Paper" and computer_choice == "Scissors") or
            (user_choice == "Scissors" and computer_choice == "Rock")):
            print("YOU LOSE :(")

