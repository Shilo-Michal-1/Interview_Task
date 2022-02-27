import json
from os import path

# Function validate a JSON file


def validate_json(json_data):
    try:
        json.loads(json_data)
        print("Given JSON string is Valid true")
    except ValueError as err:
        print("Given JSON string is Valid false,", err)
        return False
    return True


if __name__ == '__main__':

    if path.exists('valid_json.json'):
        with open(r'valid_json.json', 'r', encoding='utf-8') as f:
            json_file = f.read()
        validate_json(json_file)
    else:
        print("File path is incorrect, Please make sure the file exists")
        # output : Given JSON string is Valid True

    if path.exists('not_valid_json.json'):
        with open(r'not_valid_json.json', 'r', encoding='utf-8') as f:
            json_file = f.read()
        validate_json(json_file)
    else:
        print("File path is incorrect, Please make sure the file exists")
        # output : Given JSON string is Valid False, error
