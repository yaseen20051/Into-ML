

### A Deep Dive into Ensemble Learning on the Breast Cancer Wisconsin (Diagnostic) Dataset

This repository contains my **100% from-scratch implementation** of Decision Trees and Random Forest – no scikit-learn classifiers were used for the core algorithms (only for data loading and final comparison). Everything is built with pure Python, NumPy, Graphviz for visualizing the tree , Pandas so you can truly see what’s happening under the hood.

### Project Goal
Understand **why** Random Forest dominates single Decision Trees by building both from the ground up, watching overfitting happen in real time, and then seeing ensemble magic fix it.

### The Journey (Exactly How It Went Down)

1. **Phase 1 – The Monster Tree**  
   Started with zero restrictions → the tree kept splitting until every leaf was pure.  
   Result: a gigantic, unreadable tree with **~30+ depth** and 100% training accuracy but only ~86% on test → textbook overfitting (check the first plot, it’s hilarious and terrifying).

2. **Phase 2 – Bringing It Under Control**  
   Added classic pruning hyperparameters:  
   - `max_depth`  
   - `min_samples_split`  
   - `min_samples_leaf`  
   - `min_impurity_decrease`  

   After manual + grid search tuning → clean, interpretable tree with **90.1% test accuracy**.

3. **Phase 3 – Enter Random Forest (the hero we needed)**  
   Implemented from scratch:  
   - Bootstrap sampling (with replacement)  
   - Random subset of features at each split (√m  
   - Out-of-bag (OOB) error estimation  
   - Majority voting aggregation  

   300 trees later → **94.7% test accuracy** (81/86 test samples correct) and almost zero overfitting.  
   The variance dropped dramatically while bias stayed low — exactly why Random Forest is an industry favorite.

### Final Results

| Model                            | Test Accuracy | Correct Predictions (out of 86) | Overfitting Level |
|----------------------------------|---------------|---------------------------------|-------------------|
| Decision Tree (untuned)          | ~86%          | ~74                             | Extreme           |
| Decision Tree (tuned)            | **90.1%**     | 77                              | Moderate          |
| Random Forest (300 trees, from scratch) | **94.7%** | **81**                          | Almost none       |


### Repository Contents

```
├── DecisionTreeWithoutOptimization.ipynb # A None optimized DecisionTree
├── DecisionTree_optimized.ipynb      # Full explanation + visualization of the monster → pruned tree
├── RandomFores.ipynb      # Complete Random Forest implementation + OOB + voting
└── data/                               # Automatically downloaded via sklearn
```

### Cool Stuff Inside
- Visual of the insane untuned tree (you have to see it)
- Before/after pruning comparison
- Feature importance via mean decrease in impurity
- Accuracy vs number of trees curve
- Confusion matrices & classification reports
- Export of trees to Graphviz .dot files

### How to Run

```bash
git clone https://github.com/your-username/breast-cancer-dt-rf-from-scratch.git
cd breast-cancer-dt-rf-from-scratch
pip install -r requirements.txt
jupyter notebook
```

Just open the notebooks and run everything — works out of the box.

### Tech Stack
Python • NumPy • Pandas • Matplotlib • Seaborn • Graphviz • Scikit-learn (only for dataset & comparison)

### Why This Project Matters to Me
Building these algorithms from scratch (recursive splitting, calculating information gain at every node, handling bootstrap samples manually…) made me finally **feel** why ensemble methods are so powerful. It’s one thing to read about bagging and random subspaces — it’s another to watch 300 weak, overfitted trees vote together and suddenly beat every single model.

If you’re learning ML, I honestly recommend trying this once. The “aha” moment is worth all the debugging pain.

### Feedback Welcome!
Star if it helped  
Fork and make it better  
Open an issue if something breaks or looks ugly  
DM/comment if you just want to geek out about trees

Thanks for stopping by – happy learning!

— Yaseen Islam Mohamed 
December 2025

#MachineLearning #DataScience #Python #FromScratch #RandomForest #DecisionTree #EnsembleLearning #OpenSource #HealthcareAI #LearningInPublic