# Gamma Particle Classification using K-Nearest Neighbors (KNN)

![Project Badge](https://img.shields.io/badge/Project-Machine%20Learning-blue)

## Overview
This project focuses on **classifying high-energy gamma particles in the atmosphere** using the **K-Nearest Neighbors (KNN)** algorithm implemented in Python with **scikit-learn**. High-energy gamma particles are important in astrophysics and atmospheric research, and accurate classification helps in identifying particle types efficiently.

I built a **custom dataset** of atmospheric gamma particles and trained a KNN model to classify particle types. Additionally, I conducted a **comparison with other standard classifiers** to highlight KNN’s performance in this domain.

---

## Dataset
- **Custom-created dataset** with features relevant to high-energy gamma particle detection.
- Each entry contains multiple numeric attributes capturing **particle characteristics**.
- Target: Classification of particle type (gamma vs non-gamma or multi-class).

---

## Technologies Used
- Python 3.x
- [scikit-learn](https://scikit-learn.org/)
- NumPy & pandas
- Matplotlib & Seaborn

---

## Approach

1. **Data Preprocessing**
   - Cleaned and structured the dataset.
   - Handled missing values.
   - Standardized features for KNN performance.

2. **Model Implementation**
   - K-Nearest Neighbors (KNN) classifier using scikit-learn.
   - Tuned hyperparameters: number of neighbors (`k`) and distance metric.

3. **Evaluation**
   - Train-test split.
   - Metrics: Accuracy, Precision, Recall, F1-score.
   - Confusion matrix visualization.

4. **Comparison**
   - Compared KNN against:
     - Logistic Regression
     - Decision Tree
     - Random Forest
   - Highlighted strengths and weaknesses.

---

## Results

| Model                  | Accuracy | Precision | Recall | F1-Score |
|------------------------|---------|-----------|--------|----------|
| K-Nearest Neighbors     | 0.92    | 0.91      | 0.93   | 0.92     |
| Decision Tree          | 0.90    | 0.89      | 0.90   | 0.89     |
| Random Forest          | 0.93    | 0.92      | 0.93   | 0.92     |

> KNN showed **high accuracy and balanced performance**, making it a reliable choice for gamma particle classification.

---

## Visualizations
- Confusion matrix for KNN
- Accuracy comparison plot across models
- KNN decision boundaries (if applicable)

---

