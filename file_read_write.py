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

# error_handling_lab.py

filename = input("Enter the filename you want to read: ")

try:
    with open(filename, "r") as file:
        data = file.read()
        print("\nFile content:\n")
        print(data)
except FileNotFoundError:
    print(f"Error: The file '{filename}' does not exist.")
except PermissionError:
    print(f"Error: You do not have permission to read '{filename}'.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
