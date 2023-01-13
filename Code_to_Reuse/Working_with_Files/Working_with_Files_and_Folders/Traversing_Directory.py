import os

# Define function traverse and pass folder as a parameter
def travers(fld):
    for fldpath, dirs, fls in os.walk(fld): # Loop through each folder path, directory and files
        print(f"Folder: {fldpath}")
        for fn in fls:
            print(f"\t{fn}")

travers("")
