import random

user_wins = 0
computer_wins = 0
draw = 0
options = ["rock", "paper", "scissors"]

while True:
    users_input = input("Type Rock/Paper/Scissors or Q to Quit: ").lower()
    if users_input == "q":
        break
    if users_input not in options:
        continue
    random_number = random.randint(0, 2)
    # rock: 0, papr: 1, scissors: 2
    computer_pick = options[random_number]
    print("Computer picked ", computer_pick + ".")

    if users_input == "rock" and computer_pick == "scissors":
        print("You won!")
        user_wins += 1

    elif users_input == "paper" and computer_pick == "rock":
        print("You won!")
        user_wins += 1

    elif users_input == computer_pick:
        print("Draw!")
        draw += 1
        continue


    elif users_input == "scissors" and computer_pick == "paper":
        print("You won!")
        user_wins += 1

    else:
        print("You lost!")
        computer_wins += 1




print("You won", user_wins, "times.")
print("Computer won", user_wins, "times.")
print("Goodbye!")
