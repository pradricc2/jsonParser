import json
import sys

def is_valid_json(input_str):
    try:
        json.loads(input_str)
        return True
    except json.JSONDecodeError:
        return False

def main(file_path):
    try:
        with open(file_path, 'r') as file:
            input_str = file.read().strip()
    except FileNotFoundError:
        print(f"Error: File not found: {file_path}")
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

    if is_valid_json(input_str):
        print("Valid JSON object")
        sys.exit(0)  # Success
    else:
        print("Invalid JSON")
        sys.exit(1)  # Error

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python parser.py <file_path>")
        sys.exit(1)

    main(sys.argv[1])
