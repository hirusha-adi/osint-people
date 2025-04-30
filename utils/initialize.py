
import requests, os

def __download_file(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for any HTTP errors
        return response
    except requests.exceptions.RequestException as e:
        print(f"Error downloading file: {e}")
        return None

import os

def __save_file_to_path(url, save_path):
    folder_path = os.path.dirname(save_path)

    if not os.path.exists(folder_path):
        try:
            os.makedirs(folder_path)
            print(f"Folder '{folder_path}' created.")
        except Exception as e:
            print(f"Error creating folder: {e}")
            return
    
    file_data = __download_file(url)
    
    if file_data:
        try:
            with open(save_path, 'wb') as file:
                file.write(file_data.content)
            print(f"File saved to {save_path}")
        except Exception as e:
            print(f"Error saving file: {e}")


def initialize() -> None:
    print("Initializing the osint_people tool...")
    __save_file_to_path("https://raw.githubusercontent.com/WebBreacher/WhatsMyName/main/wmn-data.json", "support/wmn-data.json")

    print("Done!")
