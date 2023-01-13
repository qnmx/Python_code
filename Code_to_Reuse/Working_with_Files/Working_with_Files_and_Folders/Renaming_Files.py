import os
from pathlib import Path

# Define first function to rename a file
def rename_file_1(src, dst):
    os.rename(src, dst) # Invoke rename module

# Define second function to rename a file
def rename_file_2(src, dst):
    f = Path(src)
    f.rename(dst)

rename_file_1("", "")
rename_file_2("", "")