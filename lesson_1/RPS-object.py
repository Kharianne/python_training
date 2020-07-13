import random


class Game:
    OPTIONS = ["rock", "paper", "scissors"]

    def __init__(self, player_choice):
        self.player_guess = player_choice
        self.computer_guess = random.choice(Game.OPTIONS)
    
    def get_results(self):
        if self.computer_guess == self.player_guess:
            print("Tie")
            print(f"Computer guess was {self.computer_guess}")
        elif self.computer_guess == "rock" and self.player_guess == "paper":
            print("Computer wins")
            print(f"Computer guess was {self.computer_guess}")
        elif self.computer_guess == "rock" and self.player_guess == "scissors":
            print("Player wins")
            print(f"Computer guess was {self.computer_guess}")
        elif self.computer_guess == "paper" and self.player_guess == "rock":
            print("Computer wins")
            print(f"Computer guess was {self.computer_guess}")
        elif self.computer_guess == "paper" and self.player_guess == "scissors":
            print("Player wins")
            print(f"Computer guess was {self.computer_guess}")
        elif self.computer_guess == "scissors" and self.player_guess == "paper":
            print("Computer wins")
            print(f"Computer guess was {self.computer_guess}")
        elif self.computer_guess == "scissors" and self.player_guess == "rock":
            print("Player wins")
            print(f"Computer guess was {self.computer_guess}")


if __name__ == "__main__":
    while True:
        player_guess = input("What's your option: ")
        while player_guess not in Game.OPTIONS:
            player_guess = input(f"Wrong option, options are: {Game.OPTIONS}. Try again. Your option: ")
        game = Game(player_guess)
        game.get_results()
