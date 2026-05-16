# 🎬 Movie Recommender System: Matrix Factorization from Scratch

An end-to-end Machine Learning project that builds a Collaborative Filtering recommendation engine using **Matrix Factorization (SVD + SGD)**. Instead of relying on high-level library black-boxes, this project implements the core optimization math from scratch to predict personalized movie ratings and generate Top-10 recommendations.

## 🚀 Key Features

* **Custom Matrix Factorization:** Decomposes user-item interactions into latent factor matrices (P and Q) using Singular Value Decomposition (SVD) for initialization.
* **Stochastic Gradient Descent (SGD):** Custom, fully vectorized SGD implementation with L2 Regularization to optimize latent vectors and prevent overfitting.
* **Rigorous Offline Evaluation:** Splits data into strict Train (80%), Validation (10%), and Test (10%) sets to ensure zero data-leakage during the final evaluation.
* **Ranking Metrics:** Evaluates performance using real-world business metrics (`Precision@10` and `Recall@10`), moving beyond simple RMSE.
* **Latent Space Visualization:** Uses PCA to project 100-dimensional movie vectors into a 2D interactive space, revealing how the model mathematically "learned" genres without being fed text data.
* **Cosine Similarity:** A built-in KNN-style engine to find "Movies Similar to X" based on learned latent traits.

## 📊 Dataset
This project uses the **MovieLens** dataset.
* `movies_clean.csv`: Movie metadata (Titles, Genres, IDs).
* `ratings_clean.csv`: Over 100,000 user ratings across 9,700+ movies.

## 🛠️ Tech Stack
* **Python 3**
* **Data Manipulation:** `pandas`, `numpy`
* **Math & Optimization:** `scipy.sparse`, `scipy.sparse.linalg`
* **Machine Learning:** `scikit-learn` (PCA, Cosine Similarity, Metrics)
* **Data Visualization:** `matplotlib`, `seaborn`, `plotly`

## 📈 Results & Performance

The Matrix Factorization model was tested against a standard **Global Popularity Baseline** (recommending the most-rated movies to everyone). Hyperparameters (Latent Dimensions `k=20`, Regularization `λ=0.01`) were tuned on the validation set.

**Final Evaluation on Unseen Test Set:**

| Model | Precision@10 | Recall@10 |
| :--- | :--- | :--- |
| Global Popularity (Baseline) | ~ 6.5% | ~ 10.2% |
| **Matrix Factorization** | **~ 14.0%** | **~ 22.8%** |

*Conclusion:* The personalized Matrix Factorization model **more than doubled** the accuracy of the popularity baseline, successfully discovering niche, highly relevant movies for individual users.

## 🧠 Core Concepts Explored

1. **The Math of Taste:** How multiplying user vectors and item vectors predicts interaction scores.
2. **Exploding Gradients:** Addressing SVD initialization imbalances and tuning learning rates for stable gradient descent.
3. **The Cold-Start Problem:** Discussing the limitations of pure Collaborative Filtering when introducing new users or movies, and theorizing hybrid solutions.
4. **RMSE vs. Ranking:** Understanding why predicting exact star ratings (RMSE) is less important than ranking the absolute best items at the top of a user's feed (Precision@K).

## 💻 How to Run

1. Clone this repository:
   ```bash
   git clone [https://github.com/yourusername/matrix-factorization-recommender.git](https://github.com/yaseen20051/matrix-factorization-recommender.git)
