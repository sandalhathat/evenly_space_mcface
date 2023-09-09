import os
from datetime import datetime

def evenly_space_text():
    # Get user input for the text
    input_text = input("Enter the text: ")

    # Split the input text into words
    words = input_text.split()

    # Calculate the total length of all words and spaces
    total_length = len(input_text)

    # Calculate the desired space between words
    space_length = total_length // (len(words) - 1)

    # Initialize the result
    result = ""

    # Iterate through words and add spaces
    for word in words:
        result += word
        if word != words[-1]:
            result += " " * space_length

    # Generate a timestamp for the file name
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    # Create a unique file name with the timestamp
    file_name = f"esm_{timestamp}.txt"

    # Save the result to a text file
    with open(file_name, "w") as file:
        file.write(result)

    print(f"Evenly spaced text saved to {file_name}")


if __name__ == "__main__":
    evenly_space_text()
