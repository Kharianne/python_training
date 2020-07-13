import random

OPTIONS = ["rock", "paper", "scissors"]

if __name__ == "__main__":
    while True:
        player_guess = input("What's your option: ")
        while player_guess not in OPTIONS:
            player_guess = input("Wrong option, options are: rock, paper, scissors. Try again. Your option: ")
        computer_guess = random.choice(OPTIONS)
        if computer_guess == player_guess:
            print("Tie")
            print(f"Computer guess was {computer_guess}")
        elif computer_guess == "rock" and player_guess == "paper":
            print("Computer wins")
            print(f"Computer guess was {computer_guess}")
        elif computer_guess == "rock" and player_guess == "scissors":
            print("Player wins")
            print(f"Computer guess was {computer_guess}")
        elif computer_guess == "paper" and player_guess == "rock":
            print("Computer wins")
            print(f"Computer guess was {computer_guess}")
        elif computer_guess == "paper" and player_guess == "scissors":
            print("Player wins")
            print(f"Computer guess was {computer_guess}")
        elif computer_guess == "scissors" and player_guess == "paper":
            print("Computer wins")
            print(f"Computer guess was {computer_guess}")
        elif computer_guess == "scissors" and player_guess == "rock":
            print("Player wins")
            print(f"Computer guess was {computer_guess}")
        want_to_play_again = input("Wanna another game? Type: yes or no ")
        if want_to_play_again == "yes":
            continue
        else:
            break
