import json
from pathlib import Path

# Define the path to the JSON file
input_path = Path('njoftime.json')
output_path = Path('transformed_njoftime.json')

# Load the JSON data to python object (list)
data = json.loads(input_path.read_text(encoding='utf-8'))

# Convert the data to a JSON string
data_str = json.dumps(data, ensure_ascii=False)

# Replace the special characters.
data_str = data_str.replace('\u00eb', 'e')   # replaces ë with e
data_str = data_str.replace('\U0001f525', '') # replaces fire emoji to blank
data_str = data_str.replace('\u00e7', 'c')  # replaces ç with c
data_str = data_str.replace('\u00c7', 'C')  # replaces Ç with C
data_str = data_str.replace('\u00cb', 'E')  # replaces Ë with e
data_str = data_str.replace('\ufffd', '')  # replaces all other undefined to blank

# Convert the JSON string back to a Python object
transformed_data = json.loads(data_str)
content = json.dumps(transformed_data, ensure_ascii=False, indent=4)

# Save the transformed data back to a file
output_path.write_text(content, encoding='utf-8')

print(len(data))
print("Special characters replaced and data saved to 'transformed_njoftime.json'")