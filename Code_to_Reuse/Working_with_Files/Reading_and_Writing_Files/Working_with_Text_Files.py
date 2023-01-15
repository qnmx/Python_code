# Define a function to read a file all at once
# As a parameter use a name of a file
def read_txt(fn):
    with open(fn) as f: # Open a file
        print(f.read())

# Define a function to read a file line by line
def read_txt_by_line(fn):
    with open(fn) as f:
        lines = f.readlines() # Read each line in the file
        for line in lines:
            print(line, end="")
            line = f.readline()

# Define a function to write to a text file
# Text file as a parameter and the string that we want to write to the file
def write_new_txt(fn, str):
    with open(fn, "w", encoding="utf-8") as f: # Open and write to the file. Use utf-8 as an encoding type
        f.write(str) # Write to the file, pass the string to write to the file

# Define a function to append new line to a file
def append_line_txt(fn, str):
    with open (fn, "a", encoding="utf-8") as f: # Oppen a file in append mode
        f.write("\n") # Write to a file
        f.write(str)

read_txt("")
read_txt_by_line("")
write_new_txt("", "")
append_line_txt("", "")