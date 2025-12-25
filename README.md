
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

