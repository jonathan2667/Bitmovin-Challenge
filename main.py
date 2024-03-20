
from Data_Access_Layer.data_access import download_file_to_local_text_file
from Service_Layer.Services import read_file_lines, count_occurence_of_characters_in_file, sort_characters_by_occurence
from UI.ui import print_file_lines_with_numbers_in_file, print_character_occurence

url = "https://www.w3.org/TR/2003/REC-PNG-20031110/iso_8859-1.txt"
file_path = "Analysis_Files/analysis_file.txt"
output_lines_file_path = "Output/Lines_with_numbers.txt"
output_sorted_characters_occurences_file_path = "Output/Sorted_characters_occurences.txt"

def main():


    #Data Access Layer
    download_file_to_local_text_file(url, file_path)

    #Service Layer
    lines = read_file_lines(file_path)
    char_count = count_occurence_of_characters_in_file(file_path)
    sorted_characters = sort_characters_by_occurence(char_count)

    #UI Layer (Presentation Layer)
    print_file_lines_with_numbers_in_file(lines, output_lines_file_path)
    print_character_occurence(sorted_characters, output_sorted_characters_occurences_file_path)


if __name__ == "__main__":
    main()