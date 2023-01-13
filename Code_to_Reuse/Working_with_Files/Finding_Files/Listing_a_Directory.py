import os

# fld - folder
# fn - file
def list_dir(fld):
    for fn in os.listdir(fld):
        print(fn)

list_dir("")