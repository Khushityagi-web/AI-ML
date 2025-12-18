# Breast Cancer Relapse Prediction Using Clinical Data (Practice ML Project)

This project explores a small synthetic or hand-compiled clinical dataset to practice a complete machine-learning workflow for relapse prediction.

The aim of this project was skill-building, not clinical validity. The dataset is not representative of real patient cohorts.

---

## Project Overview

This practice exercise includes:

- Loading a text-based dataset into pandas  
- Cleaning inconsistent values  
- Handling missing data  
- Feature engineering  
- Categorical encoding  
- Exploring multiple label definitions (direct 0/1 vs threshold-based binarization)  
- Train/test split  
- Model training using Random Forest  
- Evaluation using metrics and ROC curve  
- Feature importance visualization  
- Hyperparameter tuning with GridSearchCV  

This project was created during my early ML learning phase to understand how different preprocessing choices affect model behavior.

---

## Preprocessing Steps

The following preprocessing steps were applied:

- Parsed a text block into a structured DataFrame  
- Removed rows with missing target values  
- Filled missing `ELSTON` values with the mean  
- Filled missing `SUBTYPE` values with `"Unknown"`  
- Combined `SUBTYPE` and `ELSTON` into a single categorical feature (experimental feature engineering)  
- One-hot encoded categorical variables  
- Normalized features using `StandardScaler`  

Two versions of the `RELAPSE` label were explored:

- Original values (0/1)  
- Threshold-based binarization (`RELAPSE > 5 → 1`, else `0`)  

---

## Model Training

A `RandomForestClassifier` was used to practice:

- Fitting machine-learning models  
- Predicting relapse outcomes  
- Interpreting predicted probabilities  
- Analyzing feature importances  

Grid search was applied to explore model parameters:

```python
param_grid = {
    'n_estimators': [50, 100, 200],
    'max_depth': [None, 10, 20],
    'min_samples_split': [2, 5, 10]
}

