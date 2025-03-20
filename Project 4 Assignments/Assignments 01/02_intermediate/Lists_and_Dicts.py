# Problem #1: List Practice
# Now practice writing code with lists! Implement the functionality described in the comments below.

# def main(): # Create a list called fruit_list that contains 
#     the following fruits: # 'apple', 'banana', 'orange', 'grape', 'pineapple'.

fruit_list = [ 'apple', 'banana', 'orange', 'grape', 'pineapple']

print(len(fruit_list))
print(fruit_list.append("mango"))
print(fruit_list)



# problem #2: Index Game
# As a warmup, read this code and play the game a few times. Use this mental model of the list:

# Objective:
# Create a Python program that helps you practice accessing and manipulating elements in a list. 
# This exercise will help you get comfortable with indexing, slicing, and modifying list elements.

# Instructions:
# Initialize a List:
# Create a list with at least 5 different elements. They can be numbers, strings, or a mix of both.

# Accessing Elements:
# Write a function that:

# Accepts a list and an index as inputs.
# Returns the element at the specified index.
# If the index is out of range, return an appropriate message.
# Modifying Elements:


# Write a function that:

# Accepts a list, an index, and a new value as inputs.
# Replaces the element at the specified index with the new value.
# If the index is out of range, return an appropriate message.
# Slicing the List:
# Write a function that:

# Accepts a list, a start index, and an end index as inputs.
# Returns a new list containing the elements from the start index up to (but not including) the end index.
# Handles cases where the indices are out of range.
# Game Interaction:
# Create a simple text-based game that:

# Prompts the user to select an operation (access, modify, slice).
# Asks for the necessary inputs (index, new value, etc.).
# Displays the result and the updated list.


def access_element(my_list, index):
    """Access an element at a specified index."""
    return my_list[index] if 0 <= index < len(my_list) else "Index out of range."

def modify_element(my_list, index, new_value):
    """Modify an element at a specified index."""
    if 0 <= index < len(my_list):
        my_list[index] = new_value
        return my_list
    return "Index out of range."

def slice_list(my_list, start_index, end_index):
    """Slice the list from start_index to end_index."""
    if 0 <= start_index < len(my_list) and 0 <= end_index <= len(my_list) and start_index < end_index:
        return my_list[start_index:end_index]
    return "Indices out of range."

def main():
    my_list = [10, "apple", 3.14, "banana", 42]

    while True:
        print("\nCurrent list:", my_list)
        choice = input("Select operation (1: Access, 2: Modify, 3: Slice, 4: Exit): ")

        if choice == '1':
            index = int(input("Enter index to access: "))
            print("Result:", access_element(my_list, index))

        elif choice == '2':
            index = int(input("Enter index to modify: "))
            new_value = input("Enter new value: ")
            print("Updated list:", modify_element(my_list, index, new_value))

        elif choice == '3':
            start_index = int(input("Enter start index for slicing: "))
            end_index = int(input("Enter end index for slicing: "))
            print("Sliced list:", slice_list(my_list, start_index, end_index))

        elif choice == '4':
            print("Exiting the game.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()