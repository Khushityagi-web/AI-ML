# Gene Expression PCA + Random Forest Workflow

This project demonstrates a complete preprocessing and modeling workflow on a gene expression dataset  
(`GSE68086_TEP_data_matrix.csv`).

The goal is to illustrate the structure of a machine-learning pipeline commonly used in computational biology.

---

## Workflow Overview

### 1. Load & Inspect Data
- Read gene expression matrix  
- Transpose data to a samples × genes structure  
- Check and handle missing values  

---

### 2. Impute & Normalize
- Mean imputation using `SimpleImputer`  
- Feature standardization using `StandardScaler`  

---

### 3. Dimensionality Reduction (PCA)
- Reduce high-dimensional gene expression data  
- Retain the top 50 principal components  
- Plot explained variance  

---

### 4. Classification (Demonstration Only)

Since the dataset contains no phenotype labels, this project uses **dummy binary labels** purely to illustrate a training pipeline.

Steps include:
- Train/test split  
- Random Forest classifier  
- Confusion matrix and ROC curve  
- Hyperparameter tuning using `GridSearchCV`  

---

### 5. Model Export
- Save the trained Random Forest model using `joblib`  

---

## Project Structure

    Gene_Expression_Model/
    │── script.py
    │── README.md

---

## Skills Demonstrated

- Working with high-dimensional omics datasets  
- Data cleaning and preprocessing  
- Dimensionality reduction using PCA  
- Machine-learning workflows (Random Forest, ROC, GridSearch)  
- Scientific visualization  
- Model serialization with `joblib`  

---

## Future Improvements

- Use real phenotype labels if available  
- Replace PCA + Random Forest with models better suited to gene expression data  
- Add feature interpretation methods (e.g., SHAP, GSEA)  
