import requests

def download_file_to_local_text_file(url, file_path):
    """
    Downloads a file from a given url to the specified file path into text format.

    We will use specific encoding, because the file is encoded as seen when accessing the specific url
    ("The following are the graphical (non-control) characters defined by ISO 8859-1 (1987).");

    :param url: User given url
    :param file_path: File path used to save.
    :return:
    """

    response = requests.get(url)

    with open(file_path, "w", encoding="iso-8859-1") as file:
        file.write(response.text)