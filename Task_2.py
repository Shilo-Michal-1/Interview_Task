import json

# Function validate a JSON file


def validate_json(json_data):
    try:
        json.loads(json_data)
    except ValueError as err:
        return False
    return True


with open(r'valid_json.json', 'r', encoding='utf-8') as f:
    json_file = f.read()
print("Given JSON string is Valid", validate_json(json_file))
# output : Given JSON string is Valid True


with open(r'not_valid_json.json', 'r', encoding='utf-8') as f:
    json_file = f.read()
print("Given JSON string is Valid", validate_json(json_file))
# output : Given JSON string is Valid False
