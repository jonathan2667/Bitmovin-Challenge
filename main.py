
from Data_Access_Layer.data_access import download_file_to_local_text_file
from Service_Layer.Services import read_file_lines, count_occurence_of_characters_in_file, sort_characters_by_occurence

def main():
    url = "https://www.w3.org/TR/2003/REC-PNG-20031110/iso_8859-1.txt"
    file_path = "Analysis_Files/analysis_file.txt"

    #Data Access Layer
    download_file_to_local_text_file(url, file_path)

    #Service Layer
    lines = read_file_lines(file_path)
    char_count = count_occurence_of_characters_in_file(file_path)
    sorted_characters = sort_characters_by_occurence(char_count)



if __name__ == "__main__":
    main()