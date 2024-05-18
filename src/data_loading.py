import pandas as pd

def load_data(filepath):
    print(f"Loading data from {filepath}")
    try:
        data = pd.read_csv(filepath, on_bad_lines='skip')
        print("Data loaded successfully.")
        return data
    except Exception as e:
        print(f"Error loading data: {e}")
        raise
