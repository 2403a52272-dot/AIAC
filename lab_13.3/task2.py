def read_file(filename):
    """Read and return file content safely."""
    try:
        with open(filename, "r") as f:
            return f.read()
    except FileNotFoundError:
        return "Error: File not found."
    except PermissionError:
        return "Error: Permission denied."
    except Exception as e:
        return f"Unexpected error: {e}"
def write_file(filename, content):
    """Write data to a file safely."""
    try:
        with open(filename, "w") as f:
            f.write(content)
        print("Written successfully")  
    except PermissionError:
        print("Error: Permission denied.")
    except Exception as e:
        print(f"Unexpected error: {e}")
choice = input("Do you want to read or write a file? (read/write): ").lower()
filename = input("Enter filename: ")
if choice == "write":
    data = input("Enter content to write: ")
    write_file(filename, data)
elif choice == "read":
    print(read_file(filename))
else:
    print("Invalid choice! Please enter 'read' or 'write'.")