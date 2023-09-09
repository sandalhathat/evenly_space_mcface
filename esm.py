import os
from datetime import datetime

def evenly_space_text():
    # Get user input for the text
    input_text = input("Enter the text: ")

    # Count the total number of spaces in the input text
    total_spaces = input_text.count(' ')

    # Split the input text into words
    words = input_text.split()

    # Calculate the total length of all words
    total_length = sum(len(word) for word in words)

    # Calculate the desired space length
    space_length = total_spaces // (len(words) - 1) if len(words) > 1 else 0

    # Initialize the result
    result = ""

    # Initialize variables to track total space and spaces placed
    total_space_placed = 0
    spaces_placed = 0

    # Iterate through words and add spaces
    for word in words:
        result += word
        if word != words[-1]:
            spaces_to_add = space_length + spaces_placed
            result += " " * spaces_to_add
            total_space_placed += spaces_to_add
            spaces_placed = space_length

    # Generate a timestamp for the file name
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    # Create a unique file name with the timestamp
    file_name = f"evenly_spaced_text_{timestamp}.txt"

    # Save the result to a text file
    with open(file_name, "w") as file:
        file.write(result)

    print(f"Evenly spaced text saved to {file_name}")
    print(f"Total spaces in input text: {total_spaces}")
    print(f"Spaces placed between terms: {total_space_placed}")


if __name__ == "__main__":
    evenly_space_text()
