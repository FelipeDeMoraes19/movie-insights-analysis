def analyze_genres(df):
    return df['genres'].value_counts().head(10)

def analyze_ratings_over_time(df):
    df['year'] = df['release_date'].dt.year
    return df.groupby('year')['vote_average'].mean()

def analyze_budget_revenue_correlation(df):
    return df[['budget', 'revenue']].corr()
