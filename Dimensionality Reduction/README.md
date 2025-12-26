# Dimensionality Reduction Experiments & Implementations

Collection of **PCA**, **Autoencoders** (and sometimes other techniques) implementations from scratch and using popular libraries.

Main goal: Understand, compare and visualize how different dimensionality reduction methods work on real and toy datasets.

## 📂 What's inside

| File/Folder                        | Description                                                                 |
|------------------------------------|-----------------------------------------------------------------------------|
| `pca.ipynb`           | Classical PCA implemented with only NumPy (SVD + eigen decomposition)       |
| `autoencoder.ipynb`         | Basic fully-connected Autoencoder (fully-connected layers)                 |


## 🎯 Main topics covered

- Classical PCA (mathematical + from scratch)
- Autoencoders vs PCA – when and why one is better
- Latent space visualization (2D/3D)
- Reconstruction quality comparison

## 🛠️ Tech stack

```text
Python 3.8+
numpy
matplotlib / seaborn
pytorch /
torchvision (for datasets & transforms)
umap-learn, sklearn.manifold (for comparison, optional)
