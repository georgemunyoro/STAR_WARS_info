import csv
from typing import List, Dict


def search_csv_file(files_to_search: List[str], **kwargs) -> List[Dict[str, str]]:
    """
    Returns a list of rows that match the given parameters
    """
    matching_rows = []
    for filepath in files_to_search:
        with open(filepath) as csv_file:
            reader = csv.DictReader(csv_file)
            for row in reader:
                for key, value in kwargs.items():
                    if type(value) == int:
                        value = str(value)

                    if key in row.keys() and value.lower() in row[key].lower():
                        matching_rows.append(row)

    return matching_rows


def search(entity_type, **kwargs) -> List[Dict[str, str]]:
    return search_csv_file(
        [f'./data/{t}.csv' for t in [
            'vehicles',
            'species',
            'starships',
            'planets',
            'characters',
        ] if entity_type == t] if entity_type != 'all' else [],
        **kwargs
    )
