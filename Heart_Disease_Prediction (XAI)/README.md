# Heart Disease Prediction with Logistic Regression + SHAP Explainability

This project demonstrates a complete machine-learning workflow using the **UCI Cleveland Heart Disease** dataset, with a focus on model interpretability using **SHAP (Explainable AI)**.

The goal is not to build a clinical-grade diagnostic model, but to practice:

- Data cleaning  
- Preprocessing  
- Logistic regression modeling  
- SHAP-based explainability  
- Model saving and loading with `joblib`  

---

## Project Overview

This repository is an ML experiment exploring how classical models behave on tabular clinical-style data. The project includes:

- End-to-end data preprocessing  
- Training a logistic regression classifier  
- Evaluating model performance  
- Applying SHAP to understand feature contributions  
- Saving and reloading both the trained model and the SHAP explainer  

---

## Dataset

- **Source:** UCI Machine Learning Repository  
- **Dataset:** Processed Cleveland Heart Disease Data  

### Target Variable
- `1` → Presence of heart disease  
- `0` → No heart disease  

Missing values (recorded as `"?"`) were dropped for simplicity.

---

## Workflow Summary

### 1. Load & Clean Data
- Replace `"?"` with `NaN`  
- Drop incomplete rows  
- Convert multiclass target into binary classification  

---

### 2. Preprocessing
- One-hot encode categorical features  
- Scale numerical features using `StandardScaler`  

---

### 3. Model Training
- Logistic Regression (`max_iter = 1000`)  
- Train/test split (80/20)  

---

### 4. Evaluation
- Accuracy  
- Classification report (precision, recall, F1-score)  

---

### 5. Explainability with SHAP
- Use `LinearExplainer`  
- Compute SHAP values on test data  
- Visualizations include:
  - Force plot (single prediction)  
  - Decision plot (multiple predictions)  

---

### 6. Model Saving

All artifacts are stored using `joblib`:

- Trained logistic regression model  
- SHAP explainer  
- SHAP value matrix  

---

## Repository Structure

    Heart_Disease_Prediction_XAI/
    │── script.py
    │── README.md

---

## Skills Demonstrated

- Classical ML on tabular biomedical data  
- Handling missing clinical variables  
- Categorical encoding and feature scaling  
- Logistic regression modeling  
- SHAP explainability fundamentals  
- Model and explainer serialization  
- Interpretation of feature contributions  

---

## Notes & Limitations

- UCI dataset is small, so results are not clinically meaningful  
- Logistic regression is inherently interpretable; SHAP here is educational  
- Dropping missing rows may introduce bias  
- No cross-validation or hyperparameter tuning included  

This project is intended as a **learning exercise**, not a diagnostic tool.

---

## Future Improvements

- Add ROC/AUC and confusion matrix  
- Try tree-based models (Random Forest, XGBoost) with SHAP TreeExplainer  
- Implement cross-validation  
- Add SHAP summary plots  
- Compare multiple models using consistent preprocessing  


