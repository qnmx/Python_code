import shutil

# Define function to move files and folders
def mv_files(src, dst):
    shutil.move(src, dst)

mv_files("", "")