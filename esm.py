def evenly_space_text(text, total_space):
    # Split the text into individual items
    items = text.split()

    # Calculate the total length of all items combined (sum)
    total_length = sum(len(item) for item in items)

    # Calculate the number of spaces between items
    num_spaces = len(items) - 1

    # Calculate the space to distribute between items
    space_between_items = (total_space - total_length) // num_spaces

    # Calculate any remaining space that couldn't be evenly distributed
    remaining_space = (total_space - total_length) % num_spaces

    # Initialize the result string
    result = items[0]

    # Iterate through the items and add spaces between them
    for i in range(1, len(items)):
        spaces = " " * space_between_items
        if i <= remaining_space:
            spaces += " "
        result += spaces + items[i]

    return result


# Testing function
text = "1234 56789 01"
total_space = 20
formatted_text = evenly_space_text(text, total_space)
print(formatted_text)
