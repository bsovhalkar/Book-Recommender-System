from scipy.sparse import load_npz
import numpy as np
import pandas as pd
from sklearn.neighbors import NearestNeighbors

def recommend(name):
    book_parse = load_npz("csr_matrix.npz")
    book_pivot = pd.read_pickle('book_pivot.pkl')
    df =  pd.read_pickle("final_rating.pkl")
    model = NearestNeighbors(algorithm='brute')
    model.fit(book_parse)
    x = book_pivot.loc[name].values.reshape(1,-1)
    distances, suggestions = model.kneighbors(x,n_neighbors=6)
    recommended = []
    for i in range(len(suggestions)):
        recommended.append(book_pivot.index[suggestions[i]])
    recommended = recommended[0].tolist()
    recommended_df = df[df['title'].isin(recommended)]
    recommended_df = (
        recommended_df
        .groupby('title', as_index=False)
        .agg(
            avg_rating=('rating', 'mean'),
            no_of_rating=('no of rating', 'max'),   # already aggregated
            author=('author', 'first'),
            publisher=('publisher', 'first'),
            year=('year', 'first')
        )
    )
    # print(recommended_df)
    return recommended_df


