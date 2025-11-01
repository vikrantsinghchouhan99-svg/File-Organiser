## 📂 File Organizer (Python Project)

This is a small Python project made by Vikrant Singh Chauhan during internship.
The project is about automatically organizing files into proper folders based on their type.
It helped me understand Python basics, file handling, and how small scripts can make daily work easier.

##💡 Project Idea

I wanted to make something simple but useful, so I decided to create a File Organizer.
The idea is that when you run the program, it checks all the files inside a folder and then automatically separates them into different folders like:

Documents

Images

Videos

Others

So we don’t have to move files manually again and again.

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
