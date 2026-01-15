"""
This module is responsible for processing the data.  It will largely contain functions that will recieve the overall dataset and 
perfrom necessary processes in order to provide the desired result in the desired format.
It is likely that most sections will require functions to be placed in this module.
"""

import csv

def load_data(file_path):
    """
    Load CSV
    Converts 'Rating' to int, 0 if null or invalid
    Returns list and the row count.
    """
    data = []
    try:
        with open(file_path, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                row['Rating'] = int(row.get('Rating', 0)) if row.get('Rating', '').isdigit() else 0
                data.append(row)
        return data, len(data)
    except FileNotFoundError:
        print(f"File not found: {file_path}")
    except Exception as e:
        print(f"Error reading file: {e}")
    return [], 0
