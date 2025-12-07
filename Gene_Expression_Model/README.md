# Gene Expression PCA + Random Forest Workflow

This project demonstrates a complete preprocessing and modeling workflow on a
gene expression dataset (`GSE68086_TEP_data_matrix.csv`).  
The goal is to illustrate the structure of a
machine-learning pipeline commonly used in computational biology.

---

## 📌 Workflow Overview

### **1. Load & Inspect Data**
- Read expression matrix
- Transpose samples × genes structure
- Check and handle missing values

### **2. Impute & Normalize**
- Mean imputation using `SimpleImputer`
- Standardization using `StandardScaler`

### **3. Dimensionality Reduction (PCA)**
- Reduce high-dimensional gene expression data  
- Retain top 50 principal components
- Plot explained variance

### **4. Classification (Demonstration Only)**
Since the dataset contains no phenotype labels, this project uses **dummy binary
labels** purely for illustrating a training pipeline.

- Train/test split  
- Random Forest classifier  
- Confusion matrix and ROC curve  
- Hyperparameter tuning (GridSearchCV)

### **5. Model Export**
- Save the trained Random Forest model with `joblib`

---

## 📂 Project Structure

Gene_Expression_Model/
│── script


---

## 🚀 Skills Demonstrated
- Working with high-dimensional omics datasets
- Data cleaning + preprocessing  
- Dimensionality reduction (PCA)
- Machine learning workflow (RF, ROC, GridSearch)
- Scientific visualization  
- Model serialization (joblib)

---

## 🔜 Future Improvements
- Use real phenotype labels if available  
- Replace PCA+RF with models better suited to gene expression  
- Add feature interpretation methods (SHAP, GSEA)

