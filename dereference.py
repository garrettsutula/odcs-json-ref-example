import yaml
import jsonref
from pathlib import Path
current_directory = Path.cwd().absolute().as_uri() + "/"
print(current_directory)

def load_and_dereference_yaml(file_path):
    with open(file_path, 'r') as f:
        raw_data = yaml.safe_load(f)
        dereferenced_data = jsonref.replace_refs(raw_data, loader=load_and_dereference_yaml,lazy_load=False,merge_props=True)
        return dereferenced_data


files_to_dereference = [
    "shipment-message.odcs.yaml",
    "shipment-table.odcs.yaml"
]

for file_path in files_to_dereference: 
    data = load_and_dereference_yaml(file_path)
    print(data)

