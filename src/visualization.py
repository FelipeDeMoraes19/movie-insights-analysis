import matplotlib.pyplot as plt
import seaborn as sns
import os

def plot_genres(genres):
    genres.plot(kind='bar', title='Gêneros Mais Populares')
    img_path = os.path.abspath(os.path.join(os.getcwd(), '..', 'images', 'popular_genres.png'))
    print(f"Saving popular_genres.png to {img_path}")
    plt.savefig(img_path)
    plt.show()

def plot_ratings_over_time(ratings_over_time):
    ratings_over_time.plot(title='Evolução das Notas ao Longo do Tempo')
    img_path = os.path.abspath(os.path.join(os.getcwd(), '..', 'images', 'ratings_over_time.png'))
    print(f"Saving ratings_over_time.png to {img_path}")
    plt.savefig(img_path)
    plt.show()

def plot_budget_revenue(df):
    sns.scatterplot(data=df, x='budget', y='revenue')
    plt.title('Correlação entre Orçamento e Receita')
    img_path = os.path.abspath(os.path.join(os.getcwd(), '..', 'images', 'budget_vs_revenue.png'))
    print(f"Saving budget_vs_revenue.png to {img_path}")
    plt.savefig(img_path)
    plt.show()
