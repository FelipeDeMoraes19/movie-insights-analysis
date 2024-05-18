import pandas as pd
import json

def load_data(filepath):
    return pd.read_csv(filepath)

def load_metadata(filepath):
    with open(filepath, 'r') as file:
        return json.load(file)
