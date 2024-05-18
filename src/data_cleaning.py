import pandas as pd

def clean_data(df):
    df['release_date'] = pd.to_datetime(df['release_date'], errors='coerce')
    df = df.dropna(subset=['title', 'genres', 'release_date', 'budget', 'revenue', 'vote_average'])
    df = df[(df['budget'] > 0) & (df['revenue'] > 0)]
    return df
