import json
from typing import List, Dict


def search_json_files(files_to_search: List[str], **kwargs) -> List[Dict[str, str]]:
    """
    Returns a list of rows that match the given parameters
    """
    matching_rows = []
    for filepath in files_to_search:
        with open(filepath) as json_file:
            reader = json.load(json_file)
            for row in reader:
                row = reader[row]
                for key, value in kwargs.items():
                    if type(value) == int:
                        value = str(value)

                    if key in row.keys() and value.lower() in row[key].lower():
                        matching_rows.append(row)

    return matching_rows


def search(entity_type: str = 'any', **kwargs) -> List[Dict[str, str]]:
    entity_types = ['vehicles', 'species', 'starships', 'planets', 'characters']
    if entity_type == 'any':
        return search_json_files([f'./data/{t}.json' for t in entity_types], **kwargs)
    return search_json_files(
        [f'./data/{t}.json' for t in entity_types if entity_type == t] if entity_type != 'all' else [], **kwargs
    )
