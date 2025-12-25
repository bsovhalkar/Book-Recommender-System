
# 📚 Book Recommendation System
This is Clustering based project

An end-to-end **Book Recommendation System** built using **Collaborative Filtering** and deployed as an interactive **Streamlit web application**.

The system recommends books based on **user–book interaction similarity**, using a sparse matrix representation and the **K-Nearest Neighbors (KNN)** algorithm.

---

## 🚀 Features

- Select a book and get similar book recommendations
- Collaborative filtering based on reader behavior
- Uses sparse matrix (`CSR`) for memory efficiency
- Average rating aggregation for clean results
- Interactive and user-friendly Streamlit UI

---

## 🧠 Recommendation Approach

This project uses **Item-Based Collaborative Filtering**:

- Books are represented as vectors in a user–item matrix
- Cosine similarity (via KNN) finds similar books
- Recommendations are based on books rated by similar users

> 📌 Similarity is derived from **user rating patterns**, not genre or content.

---

## 🗂️ Project Structure
BOOK-RECOMMENDER-SYSTEM/
│
├── __pycache__/                 # Python cache files
│
├── BX-Book-Ratings.csv          # Raw book ratings dataset
├── BX-Books.csv                 # Raw books metadata
├── BX-Users.csv                 # Raw users dataset
│
├── book_pivot.pkl               # Pivot table (Book × User matrix)
├── csr_matrix.npz               # Sparse CSR matrix for similarity computation
├── final_rating.pkl             # Cleaned & processed ratings DataFrame
│
├── recommend.py                 # Core recommendation logic (KNN-based)
├── Main.py                      # Streamlit web application (frontend)
│
├── process.ipynb                # Data preprocessing & model building notebook
│
├── requirements.txt             # Project dependencies
├── README.md                    # Project documentation
