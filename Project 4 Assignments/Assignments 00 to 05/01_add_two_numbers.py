# Problem Statement
# Write a Python program that takes two integer inputs from the user and calculates their sum. The program should perform the following tasks:

# Prompt the user to enter the first number.

# Read the input and convert it to an integer.

# Prompt the user to enter the second number.

# Read the input and convert it to an integer.

# Calculate the sum of the two numbers.

# Print the total sum with an appropriate message.

# The provided solution demonstrates a working implementation of this problem, where the main() function guides the user through the process of entering two numbers and displays their sum.

# Starter Code


# Solution 
def sum_numbers():
    print("This program sum two numbers.")
    num1 = input("Enter Your first number: ")
    num1 = int(num1)
    num2 = input("Enter Your second number: ")
    num2 = int(num2)
    total : int = num1 + num2
    print("The total is " + str(total) + ".")

sum_numbers()