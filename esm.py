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

    print(result)


if __name__ == "__main__":
    evenly_space_text()
