import argparse
import os
import re

# URL PATTERN
url_pattern = r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F]))+'

def extract_urls(input_file, output_file):
    urls = []
    try: 
        with open(input_file, 'r') as file:
            text = file.read()
            urls = re.findall(url_pattern, text)
    except FileNotFoundError:
        print(f"Input file not found: {input_file}")
        return

    # Save URLs in same Folder 
    with open(output_file, 'w') as output:
        for url in urls:
            output.write(url + '\n')

    

def main():
    # Create Parser for CLI Args
    parser = argparse.ArgumentParser(description="Extract URLs from a text a file and save them to another file")
    parser.add_argument("-f", "--input-file", required=True, help="Input Text File Containing URLs")
    parser.add_argument("-o","--output-file", required=True, help="Name Your Output Text File.")

    # Parse CLI Args
    args = parser.parse_args()

    # Get current working Directory
    current_directory = os.getcwd()

    # Create Full Path for Input and Output files
    input_file_path = os.path.join(current_directory, args.input_file)
    output_file_path = os.path.join(current_directory, args.output_file)

    #Extraction
    extract_urls(input_file_path, output_file_path)

if __name__ == "__main__":
    main()