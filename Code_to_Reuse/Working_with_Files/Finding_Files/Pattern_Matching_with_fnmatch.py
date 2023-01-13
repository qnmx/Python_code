import os, fnmatch

# fld - folder to search for
# search, search criteria
def match(fld, search):
    for fn in os.listdir(fld):
        if fnmatch.fnmatch(fn, search):
            print(fn)

match("", "")