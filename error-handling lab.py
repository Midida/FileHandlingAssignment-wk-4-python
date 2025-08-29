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
