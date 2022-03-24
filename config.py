import json
from pprint import pprint


def get_date():
    with open('candidates.json', 'r', encoding='utf-8') as file:
        date = json.load(file)
        candidates_dict = {}

        for i in date:
            candidates_dict[i["id"]] = i
        pprint(candidates_dict)
        return candidates_dict

