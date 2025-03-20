# Problem: High Low
# We want you to gain more experience working with control flow and Booleans in Python. To do this, we are going to have you develop a game! The game is called High-Low and the way it's played goes as follows:

# Two numbers are generated from 1 to 100 (inclusive on both ends): one for you and one for a computer, who will be your opponent. You can see your number, but not the computer's!

# You make a guess, saying your number is either higher than or lower than the computer's number

# If your guess matches the truth (ex. you guess your number is higher, and then your number is actually higher than the computer's), you get a point!

# These steps make up one round of the game. The game is over after all rounds have been played.

# We've provided a sample run below.

import random

def high_low_game():
    rounds = 5  
    player_score = 0

    for round_number in range(1, rounds + 1):
        player_number = random.randint(1, 100)
        computer_number = random.randint(1, 100)

        print(f"Round {round_number}:")
        print(f"Your number: {player_number}")
        print("Is your number higher or lower than the computer's number? (Type 'higher' or 'lower')")

        guess = input("Your guess: ").strip().lower()

        if (guess == 'higher' and player_number > computer_number) or (guess == 'lower' and player_number < computer_number):
            print("Correct guess! You get a point.")
            player_score += 1
        else:
            print(f"Wrong guess! The computer's number was {computer_number}.")

        print(f"Your current score: {player_score}\n")

    print(f"Game over! Your final score: {player_score} out of {rounds}")

if __name__ == "__main__":
    high_low_game()