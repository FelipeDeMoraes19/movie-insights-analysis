import pandas as pd
import ast

def extract_genres(genres_str):
    try:
        genres = ast.literal_eval(genres_str)
        return [genre['name'] for genre in genres]
    except (ValueError, SyntaxError):
        return []

def analyze_genres(df):
    df['genres'] = df['genres'].apply(extract_genres)
    all_genres = df['genres'].explode().value_counts().head(10)
    return all_genres

def analyze_ratings_over_time(df):
    df['year'] = df['release_date'].dt.year
    return df.groupby('year')['vote_average'].mean()

def analyze_budget_revenue_correlation(df):
    return df[['budget', 'revenue']].corr()
