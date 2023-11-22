#-----------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See LICENSE in the project root for license information.
#-----------------------------------------------------------------------------------------

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return app.send_static_file("index.html")

import random

def play_game():
    options = ['rock', 'paper', 'scissors']
    player_score = 0

    while True:
        player_choice = input("Choose rock, paper, or scissors: ").lower()

        if player_choice not in options:
            print("Invalid choice. Please choose rock, paper, or scissors.")
            continue

        opponent_choice = random.choice(options)

        print(f"Your opponent chose: {opponent_choice}")

        if player_choice == opponent_choice:
            print("It's a tie!")
        elif (
            (player_choice == 'rock' and opponent_choice == 'scissors') or
            (player_choice == 'scissors' and opponent_choice == 'paper') or
            (player_choice == 'paper' and opponent_choice == 'rock')
        ):
            print("You win this round!")
            player_score += 1
        else:
            print("You lose this round!")

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            break

    print(f"Your final score is: {player_score}")

if __name__ == "__main__":
    play_game()

