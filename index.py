def modify_data(content):
    # Example modification: Convert to uppercase
    return content.upper()

def read_and_write(input_file, output_file):
    try:
        # Read the input file
        with open(input_file, 'r') as infile:
            content = infile.read()
        
        # Modify the content
        modified_content = modify_data(content)
        
        # Write to the output file
        with open(output_file, 'w') as outfile:
            outfile.write(modified_content)
        
        print(f"File successfully written to {output_file}")
    
    except FileNotFoundError:
        print(f"Error: The file '{input_file}' does not exist.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Usage
input_file = "input.txt"
output_file = "output.txt"
read_and_write(input_file, output_file)
