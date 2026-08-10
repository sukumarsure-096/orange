import json
import csv

def import_data_from_json(file_path):
    login_data = []
    try:
        file = open(file_path, 'r')
        data = json.load(file)
        for row in data:
            login_data.append(tuple(row.values()))
    except Exception as e:
        print(f'while reading the json file as {e}')
        raise
    return login_data

def import_data_from_csv(file_path):
    login_data = []
    try:
        file = open(file_path, newline='', encoding='utf-8')
        data = csv.DictReader(file)
        for row in data:
            login_data.append(tuple(row.values()))
    except Exception as e:
            print(f'while reading the csv file as {e}')
            raise
    return login_data



