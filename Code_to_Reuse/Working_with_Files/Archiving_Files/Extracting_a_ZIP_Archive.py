import zipfile

# Function only extracts one file
# Pass a name of a zip file, file that will be extracted and location where the file will be extracted to
def extract_file(zipf, fn, path):
    with zipfile.ZipFile(zipf, "r") as archive: # Open a zip file in read-only mode
        archive.extract(fn, path=path) # Pass the name of a file and location for extraction

# Function extracts all files from zip file
# Pass zip file name and the path where files will be extracted to
def extract_all(zipf, path):
    with zipfile.ZipFile(zipf, "r") as archive: # Open a zip file in read-only mode
        archive.extractall(path=path) # Extract all files from zip file. Specify the path for extraction

extract_file("", "", "")
extract_all("", "")