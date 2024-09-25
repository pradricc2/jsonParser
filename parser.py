import json
import sys

# Funzione per validare un oggetto JSON
def is_valid_json_object(input_str):
    try:
        json_object = json.loads(input_str)
        return validate_json_structure(json_object)
    except json.JSONDecodeError as e:
        return f"Invalid JSON: {e.msg}"

# Funzione per validare la struttura di un oggetto JSON
def validate_json_structure(json_object):
    if not isinstance(json_object, (dict, list)):
        return "Invalid JSON: Root element is not an object or array"

    if isinstance(json_object, dict):
        return validate_dict(json_object)

    if isinstance(json_object, list):
        return validate_list(json_object)

    return "Valid JSON object with string keys and values"

# Funzione per validare il valore di un oggetto JSON
def validate_value(value):
    if isinstance(value, (str, int, float, bool, type(None))):
        return "Valid"
    elif isinstance(value, list):
        return validate_list(value)
    elif isinstance(value, dict):
        return validate_dict(value)
    else:
        return f"Invalid JSON: Value '{value}' is not a valid type"

# Funzioni per validare una lista e un dizionario
def validate_list(lst):
    for item in lst:
        value_check = validate_value(item)
        if value_check != "Valid":
            return value_check
    return "Valid"

# Funzione per validare un dizionario
def validate_dict(dct):
    for k, v in dct.items():
        if not isinstance(k, str):
            return f"Invalid JSON: Key '{k}' is not a string"
        value_check = validate_value(v)
        if value_check != "Valid":
            return value_check
    return "Valid"

# Funzione principale
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

    json_object_check = is_valid_json_object(input_str)
    print(json_object_check)
    if "Invalid" in json_object_check:
        sys.exit(1)

    sys.exit(0)

# Esecuzione del programma
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python parser.py <file_path>")
        sys.exit(1)

    main(sys.argv[1])
