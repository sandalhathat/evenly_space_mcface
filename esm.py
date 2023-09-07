import sys


def even_space_text(input_text, total_space):
    # Split the input text into terms
    terms = input_text.split()

    # Calculate the number of terms
    num_terms = len(terms)

    # Calculate the remaining space after placing the terms
    remaining_space = total_space - len(input_text) + num_terms - 1

    # Calculate the equal spacing between terms
    if num_terms > 1:
        equal_spacing = remaining_space // (num_terms - 1)
    else:
        equal_spacing = 0

    # Initialize the result string
    result = ""

    # Add the first term
    result += terms[0]

    # Add equal spacing and subsequent terms
    for i in range(1, num_terms):
        result += " " * equal_spacing + terms[i]

    return result


if __name__ == "__main__":
    # Check for the correct number of command-line arguments
    if len(sys.argv) != 3:
        print("Usage: python even_space_mcface.py [input_text] [total_space]")
    else:
        input_text = sys.argv[1]
        total_space = int(sys.argv[2])
        result_text = even_space_text(input_text, total_space)
        print(result_text)
