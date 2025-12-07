# Breast Cancer Relapse Prediction Using Clinical Data (Practice ML Project)

This project explores a small synthetic/hand-compiled clinical dataset to practice a complete machine-learning workflow for relapse prediction.  
The aim was **skill-building**, not clinical validity, and the dataset is not representative of real patient cohorts.

---

## 📌 Project Overview

This exercise includes:

- Loading a text-based dataset into pandas  
- Cleaning inconsistent values  
- Handling missing data  
- Feature engineering  
- Categorical encoding  
- Multiple label definitions (direct 0/1 vs threshold-based binarization)  
- Train/test split  
- Model training using RandomForest  
- Evaluation using metrics and ROC curve  
- Feature importance visualization  
- Hyperparameter tuning with GridSearchCV  

This was created during my early ML learning phase to understand how different preprocessing choices affect model behaviour.

---

## 🧹 Preprocessing Steps

- Parsed a text block into a structured DataFrame  
- Removed rows with missing target values  
- Filled missing ELSTON values with mean  
- Filled missing SUBTYPE values with `"Unknown"`  
- Combined `SUBTYPE + ELSTON` into a single categorical feature (experimental feature engineering)  
- One-hot encoded categorical variables  
- Normalized features using `StandardScaler`

Two versions of RELAPSE label were explored:
1. original values (0/1)  
2. threshold-based binarization (`RELAPSE > 5 → 1` else `0`)  

---

## 🤖 Model Training

A **RandomForestClassifier** was used to practice:

- fitting ML models  
- predicting relapse outcomes  
- interpreting predicted probabilities  
- analyzing feature importances  

Grid Search was applied to explore parameters:

```python
param_grid = {
    'n_estimators': [50, 100, 200],
    'max_depth': [None, 10, 20],
    'min_samples_split': [2, 5, 10]
}
