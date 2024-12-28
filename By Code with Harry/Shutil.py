import shutil
import os

shutil.copy("main.py","main1.py")
    # Copy the file main.py to main1.py


shutil.copy2("main.py","main2.py")
    # Copy the file main.py to main2.py and preserve the metadata

shutil.copytree("shri","shriyash")
    # Copy the directory/files inside of shri to shriyash

shutil.move("shri/file.txt","file.txt")
    # Move the file.txt from shri to the current directory

shutil.rmtree("shriyash")
    # Remove the directory shriyash
    # It will remove the directory and all the files inside of it

os.remove("file.txt")