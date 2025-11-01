## 📂 File Organizer using Python

This is a Python project I made to automatically organize files inside a folder based on their file types.
The project idea was given by the mentors — we had to pick one from the list, and I selected this because it’s practical and useful in daily life.

## 🧠 About the Project

The main goal of this project is to save time and keep files arranged automatically.
It checks all files inside a given folder and moves them into separate folders like Images, Documents, Videos, Audio, and Others depending on their extensions.

This helped me understand how Python handles file paths, extensions, and directory management.

## ⚙️ How It Works

The script looks inside a folder named test_files.

It reads each file’s extension (like .pdf, .jpg, .mp4, .txt, etc.).

It creates folders (if they don’t exist already).

Then moves files into the correct folders according to type.

It also uses a log file to record what changes were made or if any error occurred.

## 🧠 What I Learned

While making this project, I learned:

How to use os and shutil modules in Python.

Using loops and file paths properly.

Error handling with try-except.

Creating and updating log files using the logging module.

Testing and debugging small automation projects.

## 🚀 How to Run

Keep your sample files inside a folder named test_files.

Place that folder in the same directory as main.py.

Run this command in terminal or command prompt:

python main.py


After running, all files will be automatically moved into their respective folders.

## 📸 Screenshots

I have attached Before and After screenshots below to show the output difference.

## 📝 Notes

I tested the script using different file types like PDFs, Images, Videos, and Text files.
Also checked with some read-only files and invalid extensions to see how errors are handled.
This small project helped me a lot in understanding Python’s file handling and automation concepts.

## 🙌 Credits

**Created by Vikrant Singh Chauhan**
For internship project submission.
All code and testing done individually.
