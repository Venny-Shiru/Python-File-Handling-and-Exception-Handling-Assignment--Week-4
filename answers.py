def process_file():
    # Get input filename from user
    input_filename = input("Enter the name of the file to read: ")
    
    # Try to open and read the input file
    try:
        with open(input_filename, 'r') as input_file:
            content = input_file.read()
    except FileNotFoundError:
        print(f"Error: File '{input_filename}' was not found.")
        return
    except PermissionError:
        print(f"Error: You don't have permission to read '{input_filename}'.")
        return
    except IsADirectoryError:
        print(f"Error: '{input_filename}' is a directory, not a file.")
        return
    except Exception as e:
        print(f"Error reading the file: {e}")
        return
    
    # Get output filename
    output_filename = input("Enter the name for the output file: ")
    
    # Modify the content 
    modified_content = content.upper()
    
    # Write the modified content to the output file
    try:
        with open(output_filename, 'w') as output_file:
            output_file.write(modified_content)
        print(f"Successfully wrote modified content to '{output_filename}'.")
    except PermissionError:
        print(f"Error: You don't have permission to write to '{output_filename}'.")
    except IsADirectoryError:
        print(f"Error: '{output_filename}' is a directory, not a file.")
    except Exception as e:
        print(f"Error writing to the file: {e}")

if __name__ == "__main__":
    process_file()
