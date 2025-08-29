# file_read_write.py

# Read from input.txt and write uppercase content to output.txt
try:
    with open("input.txt", "r") as infile:  # Open input file
        content = infile.read()            # Read all content

    modified_content = content.upper()     # Modify content (uppercase)

    with open("output.txt", "w") as outfile:  # Write to new file
        outfile.write(modified_content)

    print("File has been read and modified successfully!")

except FileNotFoundError:
    print("Error: input.txt not found. Please make sure the file exists.")

