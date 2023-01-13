import os

# Define a new function and pass a file to delete as a parameter
def remove_file(f):
    if os.path.isfile(f): # check if parameter is a file, use isfile() method
        try:
            os.remove(f) # Call remove() method, passing the file to remove
        except OSError as e: # If during file deletion an error occurs:
            print(f"Error: {f} : {e.strerror}") # Print the error that occured
    else: # If file if a folder
        print(f"Error: {f} is not a valid file")

remove_file("")