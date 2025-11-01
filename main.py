# File Organizer Project
# This program helps to arrange all files in a folder based on their types.
# I made this to automatically move documents, images, videos etc. into separate folders.

import os
import shutil

# this is the folder where all files are kept
source_folder = "test_files"

# here i created categories for different file types
folders = {
    "Documents": [".pdf", ".docx", ".txt"],
    "Images": [".jpg", ".jpeg", ".png"],
    "Videos": [".mp4", ".mkv", ".avi"],
    "Music": [".mp3", ".wav"]
}

# this function will check file extension and tell which folder it should go
def get_folder_name(extension):
    for folder_name, extensions in folders.items():
        if extension.lower() in extensions:
            return folder_name
    return "Others"

# this part will go through all files and move them to correct folders
def organize_files():
    for file_name in os.listdir(source_folder):
        file_path = os.path.join(source_folder, file_name)

        # skip if it's already a folder
        if not os.path.isfile(file_path):
            continue

        # getting the extension of the file
        _, extension = os.path.splitext(file_name)
        folder_name = get_folder_name(extension)
        folder_path = os.path.join(source_folder, folder_name)

        # make new folder if it doesn’t exist
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

        # move the file into that folder
        shutil.move(file_path, folder_path)
        print(f"Moved: {file_name} → {folder_name}/")

    print("\nAll files organized successfully!")

# main function
if __name__ == "__main__":
    print("Organizing files in 'test_files' folder...")
    organize_files()
