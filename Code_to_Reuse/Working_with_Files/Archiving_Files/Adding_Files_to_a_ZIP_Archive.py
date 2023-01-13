import zipfile

# List of files that will be added to exsiting zip file
to_add = ["", ""]

# Define function
# Pass zip file name, the list of files to add and additional parameters
def add_to_zip(zipf, files, opt):
    with zipfile.ZipFile(zipf, opt) as archive:
        for f in files:
            lst = archive.namelist() # get a list of files in z zip file
            if not f in lst: # Check if the files does not exist in the zip file
                archive.write(f) # Add exisitng file to a zip
            else: # If the files exist in the zip file
                print(f"File exists in zip: {f}")

# "a" option will open a zip file and append new files
add_to_zip("", to_add, "a")