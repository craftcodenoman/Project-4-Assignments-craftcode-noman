# Problem Statement
# Guess My Number

# I am thinking of a number between 0 and 99... Enter a guess: 50 Your guess is too high

# Enter a new number: 25 Your guess is too low

# Enter a new number: 40 Your guess is too low

# Enter a new number: 45 Your guess is too low

# Enter a new number: 48 Congrats! The number was: 48

# Solution

import random
original_number = random.randint(0, 50)

while True:
    guessed_number = int(input("Enter Your Number: "))

    if original_number < guessed_number:
        print("Your number is to high")
    elif original_number > guessed_number:
        print("Your number is too low")
    else:
        print("Congratulation!🎉  Your number is correct")
        break