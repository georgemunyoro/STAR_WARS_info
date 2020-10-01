import csv
import json
from typing import List


def search_csv_file(files_to_search: List[str], **kwargs) -> str:
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

                    if key in row.keys() and row[key] == value:
                        matching_rows.append(row)

    return json.dumps(matching_rows)


def search_characters(**kwargs) -> str:
    return search_csv_file(["./data/characters.csv"], **kwargs)


def search_planets(**kwargs) -> str:
    return search_csv_file(["./data/planets.csv"], **kwargs)


def search_starships(**kwargs) -> str:
    return search_csv_file(["./data/starships.csv"], **kwargs)


def search_species(**kwargs) -> str:
    return search_csv_file(["./data/species.csv"], **kwargs)


def search_vehicles(**kwargs) -> str:
    return search_csv_file(["./data/vehicles.csv"], **kwargs)


def search_all(**kwargs) -> str:
    return search_csv_file(
        [
            "./data/vehicles.csv",
            "./data/species.csv",
            "./data/starships.csv",
            "./data/planets.csv",
            "./data/characters.csv",
        ],
        **kwargs
    )
