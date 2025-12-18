# AI Pipeline for Cancer Dataset Search & Analysis

This project implements a simple end-to-end workflow for searching, downloading, preprocessing, analyzing, and modeling cancer-related datasets using public **NCBI GEO** resources.

It was created during my early AI/ML learning phase and focuses on understanding how real-world biomedical data pipelines work.

---

## Project Overview

This pipeline demonstrates:

- Automated dataset search through the NCBI Entrez API  
- Metadata extraction (title, organism, samples, platform)  
- Automated dataset download and archive extraction  
- Structured preprocessing (missing values, encoding, normalization)  
- Training and evaluating a Random Forest classifier  
- Hyperparameter tuning using GridSearchCV  
- Feature importance extraction  
- Basic ML deployment using FastAPI for prediction  

The primary purpose of this project is **workflow learning**.

---

## Pipeline Steps

### 1. Search GEO Datasets (Entrez API)

The script submits a query such as:

    "breast cancer AND relapse"

It retrieves:

- Dataset IDs  
- Titles  
- Organism  
- Platforms  
- Sample counts  
- FTP download links  

---

### 2. Download and Extract Datasets

The pipeline:

- Creates a `datasets/` folder  
- Downloads `.tar.gz`, `.zip`, or flat files  
- Detects archive type automatically  
- Extracts files into organized subfolders  

---

### 3. Metadata Summary

Collected metadata is saved to:

    datasets/metadata.csv

Fields include:

| Field     | Meaning            |
|-----------|--------------------|
| ID        | GEO dataset ID     |
| Title     | Dataset title      |
| Organism  | Species            |
| Platform  | Technology used    |
| Samples   | Sample count       |
| FTPLink  | Download URL       |

---

### 4. Preprocessing

Each dataset undergoes the following steps.

#### Missing Value Handling
- Numeric values → mean  
- Categorical values → `"Unknown"`  
- Target (`RELAPSE`) rows optionally dropped if missing  

#### Encoding Categorical Variables
- One-hot encoding applied  

#### Normalization
- `StandardScaler` applied to numeric columns  

All processed datasets are saved to:

    preprocessed_datasets/

A synthetic example dataset is also generated for demonstration purposes.

---

### 5. Machine Learning Model

A Random Forest classifier is trained with:

- Train/test split  
- 5-fold cross-validation  
- Confusion matrix  
- ROC curve and AUC  
- Hyperparameter tuning (`n_estimators`, `max_depth`, etc.)  
- Feature importance visualization  

The final trained model is saved as:

    breast_cancer_model.pkl

---

### 6. Deployment via FastAPI

The API:

- Loads the trained model  
- Accepts JSON inputs  
- Returns the predicted class (0/1)  
- Returns the relapse probability score  

**Example output:**

```json
{
  "prediction": 1,
  "probability": 0.87
}
