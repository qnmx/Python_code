import shutil

# Define function to copy files
def copy_file(src, dst):
    shutil.copy(src, dst)

# Define function to copy folders
def copy_folder(src, dst):
    shutil.copytree(src, dst)


copy_file("", ".")
copy_folder("", "")