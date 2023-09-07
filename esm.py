import sys


def even_space_text(input_text):
    # Calculate the total space based on the length of the input string
    total_space = len(input_text)

    # Split the input text into terms
    terms = input_text.split()

    # Calculate the space between each term
    space_between_terms = total_space // (len(terms) - 1)

    # Initialize the result string
    result = ""

    # Iterate through the terms and add them with spaces
    for term in terms[:-1]:
        result += term + " " * space_between_terms

    # Add the last term without extra space
    result += terms[-1]

    return result


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python even_space_mcface.py <input_text>")
        sys.exit(1)

    input_text = sys.argv[1]
    output_text = even_space_text(input_text)
    print(output_text)
