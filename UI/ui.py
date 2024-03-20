
def print_file_lines_with_numbers_in_file(lines, file_to_print):
    """
    Prints the lines of the file with line numbers.

    :param lines: List of lines in the file
    :param file_to_print: Text file to print
    :return:
    """

    with open(file_to_print, "w") as file:
        file.write("Starting to print file lines with numbers:\n\n")
        for i, line in enumerate(lines, 1):
            file.write(f"Line {i}: {line}")

    #We will also print in the console
    print("\nFile Lines:\n\n")
    for i, line in enumerate(lines, 1):
        print(f"Line {i}: {line}")

def print_character_occurence(char_count, file_to_print):
    """
    Prints the character occurences in the file.

    To avoid endline problems we will print \n for newlines. If we do not do this, the file will not be printed correctly and the lines will be mixed.

    :param char_count: Dictionary with characters and their occurences
    :param file_to_print: Text file to print
    :return:
    """

    with open(file_to_print, "w") as file:
        file.write("Starting to print character occurences:\n\n")
        for char, count in char_count:
            if char == '\n':
                file.write(f"'\\n': {count}\n")
            else:
                file.write(f"'{char}': {count}\n")

    #We will also print in the console
    for char, count in char_count:
        if char == '\n':
            print(f"'\\n': {count}")  # Print \n for newlines
        else:
            print(f"'{char}': {count}")