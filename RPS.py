import random

player_score = 0
computer_score = 0

options = ["ROCK","PAPER","SCISSORS"]
print("Welcome to rock, paper, scissors !\n")
print("When prompted, choose one of the three and try to beat the computer.\n")
print("Type 'end' at any point to end the game and see the final score\n")

while True:
    computer_choice = random.choice(options)

    player_choice = input("Rock, paper or scissors?").upper()

    if player_choice == computer_choice:
        print(f"The computer chose {computer_choice}!")
        print("It's a draw!")
    elif player_choice == "ROCK":
        if computer_choice == "PAPER":
          print(f"The computer chose {computer_choice}!")
          print("You lose!")
          computer_score = computer_score + 1
        else:
          print(f"The computer chose {computer_choice}!")
          print("You win!")
          player_score = player_score + 1
    elif player_choice == "PAPER":
        if computer_choice == "SCISSORS":
          print(f"The computer chose {computer_choice}!")
          print("You lose!")
          computer_score = computer_score + 1
        else:
          print(f"The computer chose {computer_choice}!")
          print("You win!")
          player_score = player_score + 1
    elif player_choice == "SCISSORS":
        if computer_choice == "ROCK":
          print(f"The computer chose {computer_choice}!")
          print("You lose!")
          computer_score = computer_score + 1
        else:
          print(f"The computer chose {computer_choice}!")
          print("You win!")
          player_score = player_score + 1
    elif player_choice == "END":
       print(f"Final score: \nComputer {computer_score} - {player_score} Player")
       break
    else:
       print("Please enter one of the following: rock, paper, scissors, end")