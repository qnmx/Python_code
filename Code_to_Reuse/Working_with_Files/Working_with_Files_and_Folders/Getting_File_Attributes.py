import os
from datetime import datetime

# Define a function that will return UTC date time
# strftime(%d %b %Y) convert to a str
def get_date(timestmp):
    return datetime.utcfromtimestamp(timestmp).strftime("%d %b %Y")

# Get attribute function
# fld - folder
def get_file_attrs(fld):
    with os.scandir(fld) as dir: # Scan directory
        for f in dir:
            if f.is_file(): # Check if folder is a file
                inf = f.stat() # Return statistics for a file
                print(f"Modified {get_date(inf.st_mtime)} {f.name}")

get_file_attrs("")