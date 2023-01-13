import os

# fld - folder to search for
# search, search criteria
def ends_with(fld, search):
    for fn in os.listdir(fld):
        if fn.endswith(search):
            print(fn)

def start_with(fld, search):
    for fn in os.listdir(fld):
        if fn.startswith(search):
            print(fn)

ends_with("", "")
start_with("", "")