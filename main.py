
from data_access import download_file_to_local_text_file

def main():
    url = "https://www.w3.org/TR/2003/REC-PNG-20031110/iso_8859-1.txt"
    file_path = "analysis_file.txt"

    download_file_to_local_text_file(url, file_path)

if __name__ == "__main__":
    main()