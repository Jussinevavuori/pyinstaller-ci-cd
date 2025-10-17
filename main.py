import argparse
import json
import os
from rxmockup.main import run 

def dir_path(string):
    # Create the directory if it doesn't exist
    if not os.path.exists(string):
        os.makedirs(string, exist_ok=True)
    
    if os.path.isdir(string):
        return string
    else:
        raise NotADirectoryError(f"Unable to create or access directory: {string}")

def parse_args():
    parser = argparse.ArgumentParser(description="rxmockup")
    parser.add_argument('--input', dest="json", type=str, required=True, help='JSON input string')
    parser.add_argument('--output-files-dir', dest="output_file_dir", type=dir_path, required=True, help='Directory for produced files')
    return parser.parse_args()

def main():
    args = parse_args()

    try:
        json_data = json.loads(args.json)
    except json.JSONDecodeError as e:
        print(f"Invalid JSON: {e}")
        return

    # Pass parsed arguments to your application logic
    run(json_data, args.output_file_dir)

if __name__ == "__main__":
    main()