import csv

# Define function to read CSV files
# Pass a name of CSV file to read and a CSV delimiter
def read_csv(fn, delimiter):
    with open(fn) as csv_f: # Open CSV file
        cnt = -1
        rows = csv.reader(csv_f, delimiter = delimiter) # Read rows from the CSV
        for r in rows: # Look at each row in CSV file
            if cnt == -1:
                print(f'{" | ".join(r)}') # Print the header of the CSV file
            else:
                print(f"{r[0]} | {r[1]} | {r[2]} | {r[3]}") # Print each of the value for the current row
            cnt += 1 # For each loop increment the value of the counter
        print(f'{cnt} lines')

# Function that writes to the CSV files
# Pass the CSV file name, header and a row data
def write_csv(fn, header, row):
    with open(fn, mode="w", newline="") as csv_f: # Open CSV filer in write mode. Newline start with ""
        writer = csv.writer(csv_f, delimiter=",", quotechar='"', quoting=csv.QUOTE_MINIMAL) # Invoke writer() method to be able to write, to CSV file
        writer.writerow(header) # Write to the CSV file
        writer.writerow(row)

read_csv("", "")
write_csv("",
["", "", "", ""], # header
["", "", "", ""]) # row