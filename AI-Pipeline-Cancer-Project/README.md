# AI Pipeline for Cancer Dataset Search & Analysis

This project implements a simple end-to-end workflow for searching, downloading, preprocessing, analyzing, and modeling cancer-related datasets using public NCBI GEO resources.  
It was created during my early AI/ML learning phase and focuses on understanding how real-world biomedical data pipelines work.

---

## 🔍 Project Overview

This pipeline demonstrates:

- Automated dataset search through **NCBI Entrez API**
- Metadata extraction (title, organism, samples, platform)
- Automated dataset download + archive extraction
- Structured preprocessing (missing values, encoding, normalization)
- Training & evaluating a Random Forest classifier
- Hyperparameter tuning with GridSearchCV
- Feature importance extraction
- Basic ML deployment using **FastAPI** for prediction

The purpose is workflow learning. 

---

## 🚀 Pipeline Steps

### **1️⃣ Search GEO Datasets (Entrez API)**  
The script submits a query such as: "breast cancer AND relapse"

And retrieves:

- Dataset IDs  
- Titles  
- Organism  
- Platforms  
- Sample counts  
- FTP download links  

---

### **2️⃣ Download + Extract Datasets**

The pipeline:

- Creates a `datasets/` folder
- Downloads `.tar.gz`, `.zip`, or flat files
- Detects archive type automatically
- Extracts files into organized subfolders

---

### **3️⃣ Metadata Summary**

Collected metadata is saved into: datasets/metadata.csv

Fields include:

| Field | Meaning |
|-------|---------|
| ID | GEO dataset ID |
| Title | Dataset title |
| Organism | Species |
| Platform | Technology used |
| Samples | Sample count |
| FTPLink | Download URL |

---

### **4️⃣ Preprocessing**

Each dataset undergoes:

#### ✔ Missing Value Handling  
- Numeric → mean  
- Categorical → `"Unknown"`  
- Target (`RELAPSE`) rows optionally dropped if missing  

#### ✔ Encoding Categorical Variables  
Using one-hot encoding.

#### ✔ Normalization  
`StandardScaler` applied to numeric columns.

All processed datasets are saved to: preprocessed_datasets

A synthetic example dataset is also generated for demonstration.

---

### **5️⃣ Machine Learning Model**

A Random Forest classifier is trained with:

- Train/test split  
- 5-fold cross-validation  
- Confusion matrix  
- ROC curve + AUC  
- Hyperparameter tuning (`n_estimators`, `max_depth`, etc.)  
- Feature importance visualization  

Final model saved as: breast_cancer_model.pkl

---

### **6️⃣ Deployment via FastAPI**

The API:

- Loads the trained model
- Accepts JSON inputs
- Returns the predicted class (0/1)
- Returns the relapse probability score

Example output:

```json
{
  "prediction": 1,
  "probability": 0.87
}
