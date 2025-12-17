import csv
import os

# Get the directory of the current script
script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, "phonebook.csv")

# file=open(file_path, "a", newline="")

# name=input("Enter name: ")
# number=input("Enter number: ")

# writer=csv.writer(file)
# writer.writerow([name, number])
# file.close()

# Or

# with open(file_path, "a",newline="") as file:
#     name=input("Enter name: ")
#     number=input("Enter number: ")
#     writer=csv.writer(file)
#     writer.writerow([name, number])


# Saving As Dictionary

with open(file_path, "a",newline="") as file:
    name=input("Enter name: ")
    number=input("Enter number: ")
    writer=csv.DictWriter(file, fieldnames=["name", "number"])
    writer.writeheader()
    writer.writerow({"name": name, "number": number})