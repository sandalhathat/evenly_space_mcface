from datetime import datetime

def evenly_space_text():
    # Get user input for the text
    input_text = input("Enter the text: ")

    # Split the input text into words
    words = input_text.split()

    # Calculate the total number of spaces needed to evenly distribute
    total_spaces = len(words) - 1

    # Calculate the number of spaces to place between terms
    spaces_between_terms = len(input_text) - len("".join(words))

    # Calculate the total length of the output string
    total_length = len(input_text) + spaces_between_terms

    # Initialize the result
    result = ""

    # Iterate through words and add spaces
    for i, word in enumerate(words):
        result += word
        if i < len(words) - 1:
            spaces_to_add = " " * (spaces_between_terms // total_spaces)
            result += spaces_to_add

    # Generate a timestamp for the file name
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    # Create or append to the "output.txt" file
    with open("output.txt", "a") as file:
        file.write(f"Total spaces in input text: {total_length}\n")
        file.write(f"Spaces placed between terms: {spaces_between_terms}\n")
        file.write(f"Evenly spaced text: \"{result}\"\n\n")

    print(f"Total spaces in input text: {total_length}")
    print(f"Spaces placed between terms: {spaces_between_terms}")
    print(f"Evenly spaced text saved to output.txt")


if __name__ == "__main__":
    evenly_space_text()
