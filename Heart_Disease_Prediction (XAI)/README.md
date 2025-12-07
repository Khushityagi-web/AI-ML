# Heart Disease Prediction with Logistic Regression + SHAP Explainability

This project demonstrates a complete machine-learning workflow using the
UCI Cleveland Heart Disease dataset — with a focus on **model interpretability**
using SHAP (XAI).

The goal is not to build a clinical-grade diagnostic model, but to practice:
- data cleaning  
- preprocessing  
- logistic regression  
- SHAP explainability  
- model saving/loading with joblib  

---

## 📌 Project Overview

This repository is an ML experiment where I explored how classical
models behave on tabular clinical-style data. The project includes:

- End-to-end data preprocessing  
- Training a logistic regression classifier  
- Evaluating model performance  
- Applying SHAP to understand feature contributions  
- Saving and reloading both the model and the explainer  

---

## 📊 Dataset

**Source:** UCI Machine Learning Repository  
**Dataset:** Processed Cleveland Heart Disease Data  
**Target:**  
- `1` → presence of heart disease  
- `0` → no heart disease  

Missing values (recorded as `"?"`) were dropped for simplicity.

---

## 🔄 Workflow Summary

### **1. Load & Clean Data**
- Replace `"?"` with NaN  
- Drop incomplete rows  
- Convert multiclass target into binary classification  

### **2. Preprocessing**
- One-hot encode categorical features  
- Scale numerical features using `StandardScaler`

### **3. Model Training**
- Logistic Regression (`max_iter=1000`)  
- Train/test split (80/20)

### **4. Evaluation**
- Accuracy  
- Classification report (precision, recall, F1)

### **5. Explainability with SHAP**
- Use `LinearExplainer`  
- Compute SHAP values on test data  
- Visualize:
  - force plot (single prediction)
  - decision plot (multiple predictions)

### **6. Model Saving**
All stored using `joblib`:
- trained model  
- SHAP explainer  
- SHAP value matrix  

---

## 📁 Repository Structure
Heart_Disease_Prediction_XAI/
│── script


---

## 🧠 Skills Demonstrated

- Classical ML on tabular biomedical data  
- Handling missing clinical variables  
- Categorical encoding + scaling  
- Logistic regression modeling  
- SHAP explainability fundamentals  
- Model and explainer serialization  
- Interpretation of feature contributions  

---

## ⚠ Notes & Limitations

- UCI dataset is small → results are **not clinically meaningful**  
- Logistic regression is inherently interpretable → SHAP here is educational  
- Dropping missing rows may introduce bias  
- No cross-validation or hyperparameter tuning included  

This project is meant as a **learning exercise**, not a real diagnostic tool.

---

## 🔧 Future Improvements

- Add ROC/AUC and confusion matrix  
- Try tree-based models (Random Forest, XGBoost) + SHAP TreeExplainer  
- Implement cross-validation  
- Add SHAP summary plots  
- Compare multiple models using consistent preprocessing  



