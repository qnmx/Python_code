import zipfile

# Create a list with files that will be archived
to_zip = ["", ""]

# Define function and pass parameters: name of the zip files, the list of files to compress and additional zip options
def create_zip(zipf, files, opt):
    with zipfile.ZipFile(zipf, opt, allowZip64=True) as archive: # Create a zip file that will containt files to compress
        for f in files: # Add file to a zip file
            archive.write(f)
# First parameter: name of the zip file
# Second paramter: file to be added to the archive
# Third parameter: addtional options, "w", add file to archive
create_zip("", to_zip, "w")