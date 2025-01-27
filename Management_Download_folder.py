'''             **********       FILE MANAGEMENT ON DOWNLOADS FOLDER PROGRAM         *****************
      
Make an application designed to improve the organization of a computer's download folder.
.............The program creates folders for each format with the name of the file extension 
.............after automatically classifying files based on their extensions. 
.............The folder is effectively cleaned using this technique, and 
..............similar files are logically arranged into the proper directories.

                                   *************** Pseudocode   ********************
                                   
Step1 .............Go for Import necessary libraries from os and glob
Step2 ..............Go for discover a list of files in the current directory in root of Downloads folder
Step3 ..............Create a set to store unique file extensions
Step4 ..............Process a iterate through each file in the list
Step5 ..............Create a function to create folders for each unique extension
Syep6 ..............Create a function to move files to their respective folders
Step7 ..............Call the functions to perform the file management operations

                                 *****************      Start Program     *************
                                 
Description ...........Create a program that works through any paragraph and counts 
..................the number of times the letters (a, j,d,e, l) do NOT occur in a word
..................Paragraph which is default.
Author .................Mohammadreza Habibinejadnad Kochesfehani
Date ..................01/09/2023,05/09/2023,08/09/2023
time ................... 6:15 PM,9:20 PM, 5:30 PM
version ................ 1.0---- made program
version ................ 2.0 ---made Function for Creating folder and Moving the files
version ................ 3.0 --- Exception handelling if files is open and print error message
version ................ 4.0 ---Improvements made: Used os.path.splitext to split the filename and extension,
........................which is more robust than splitting by, and handles filenames with multiple dots correctly.
........................then added exception handling for folder creation and file movement to handle possible errors more gracefully.
........................Skipped ".py" files during folder creation and file movement.
........................Printed error messages for any exceptions that occur during the process.
...................This code should be more resilient when dealing with unexpected situations like file not found or destination file already exists.
           **********************************                    ***********************************************
'''
# # Import necessary libraries
import os
import glob
import shutil

# Discover a list of files in the current directory
files_list = glob.glob('*')

# Create a set to store unique file extensions
extensions_set = set()

# Iterate through each file in the list
for each_file in files_list:
    # Split the filename to get the extension
    _, extension = os.path.splitext(each_file)
    extensions_set.add(extension)

# Create a function to create folders for each unique extension using os.makedirs


def create_folders():
    for ext in extensions_set:
        if ext == '.py':
            continue
        try:
            # Remove the dot from the extension
            os.makedirs(ext[1:] + '_files')
        except FileExistsError:
            pass  # If the folder already exists, continue

# Create a function to move files to their respective folders using shutil.move


def move_files():
    # Iterate through each file in the 'files_list'
    for each_file in files_list:
        # Split the file name and extension using 'os.path.splitext'
        _, extension = os.path.splitext(each_file)

        # Skip Python (.py) files, as we don't want to move them
        if extension == '.py':
            continue

        try:
            # Attempt to move the file to a folder named after its extension
            # - 'shutil.move' is used to move files
            # - 'each_file' is the source file path
            # - 'extension[1:]' extracts the extension without the leading dot
            # - '_files/' is added to specify the destination folder
            # - 'each_file' is appended at the end to preserve the file name
            shutil.move(each_file, extension[1:] + '_files/' + each_file)

        except FileNotFoundError:
            # Handle the case when the source file does not exist
            print(f"File not found: {each_file}")

        except FileExistsError:
            # Handle the case when a file with the same name already exists
            # in the destination folder
            print(f"File already exists in destination: {each_file}")


# Call the functions to perform the file management operations
try:
    create_folders()
    move_files()
except Exception as e:
    print(f"An error occurred: {str(e)}")


'''                       *************                End Program               ***************'''
