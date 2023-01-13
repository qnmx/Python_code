from pathlib import Path

# fld - folder to search for
# search, search criteria
def glob_match(fld, search):
    p = Path(fld) # Get the path for the folder that will be inspected
    for n in p.glob(search):
        print(n)

glob_match("", "")