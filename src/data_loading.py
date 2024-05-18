import pandas as pd
import json

def load_data(filepath):
    return pd.read_json(filepath, lines=True)

def load_metadata(filepath):
    with open(filepath, 'r') as file:
        return json.load(file)
