import json


def extract_table_name(json_data):
    table_name = list(json_data.keys())[0]
    return table_name


def extract_keys(json_data):
    table_name = extract_table_name(json_data)
    if table_name in json_data:
        keys = list(json_data[table_name].keys())
        return keys
    else:
        return []


def extract_values(json_data):
    table_name = extract_table_name(json_data)
    if table_name in json_data:
        keys = list(json_data[table_name].values())
        return keys
    else:
        return []
