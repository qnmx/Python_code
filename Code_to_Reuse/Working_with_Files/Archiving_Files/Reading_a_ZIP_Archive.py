import zipfile

# Define function
# Pass the name of the zip file that we want to read
def read_zip(zipf):
    with zipfile.ZipFile(zipf, "r") as archive: # To open a zip file in read mode
        lst = archive.namelist() # Check what files exists in zip file
        for l in lst:
            zfinf = archive.getinfo(l) # For each file found in the zip file call .getinfo()
            print(f"{l} => {zfinf.file_size} bytes, {zfinf.compress_size} compressed") # Print file details

# Invoke read_zip() function and pass the zip file to read
read_zip("")