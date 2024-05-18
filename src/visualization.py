import matplotlib.pyplot as plt
import seaborn as sns

def plot_genres(genres):
    genres.plot(kind='bar', title='Gêneros Mais Populares')
    plt.savefig('images/popular_genres.png')
    plt.show()

def plot_ratings_over_time(ratings_over_time):
    ratings_over_time.plot(title='Evolução das Notas ao Longo do Tempo')
    plt.savefig('images/ratings_over_time.png')
    plt.show()

def plot_budget_revenue(df):
    sns.scatterplot(data=df, x='budget', y='revenue')
    plt.title('Correlação entre Orçamento e Receita')
    plt.savefig('images/budget_vs_revenue.png')
    plt.show()
