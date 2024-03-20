
def read_file_lines(file_path):
    """
    Reads the file and returns a list of lines
    :param file_path: User's file path
    :return:
    """

    with open(file_path, "r", encoding="iso-8859-1") as file:
        return file.readlines()
def count_occurence_of_characters_in_file(file_path):
    """
    Counts the occurence of each character in the file and returns a dictionary with results
    :param file_path: User's file path
    :return:
    """

    char_count = {}

    with open(file_path, "r", encoding="iso-8859-1") as file:
        for line in file:
            for char in line:
                if char in char_count:
                    char_count[char] += 1
                else:
                    char_count[char] = 1

    return char_count

def sort_characters_by_occurence(char_count):
    """
    Sorts the characters by occurence and returns a list of tuples
    :param char_count: Dictionary of characters and their occurence
    :return:
    """

    items_list = list(char_count.items())
    items_list.sort(key=lambda x: x[1], reverse=True)
    return items_list