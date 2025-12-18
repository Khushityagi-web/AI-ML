# Biomarker Prediction Using Logistic Regression (R)

This project demonstrates a simple and interpretable machine-learning workflow for predicting breast cancer status using metabolic and hormonal biomarkers.

It was created during my early R learning phase to understand how classical statistical models behave on biomedical data.

---

## Project Overview

This workflow includes:

- Data loading and cleaning  
- Handling missing values  
- Train/test split (70/30)  
- Logistic regression model training  
- Confusion matrix and accuracy metrics  
- ROC curve and AUC calculation  
- Predicted vs actual visualization  
- Coefficient and p-value extraction  

The focus of this project is to practice **interpretability and model understanding**, not to build a clinical model.

---

## File Structure

    Biomarker_Prediction/
    │── script.R
    │── README.md

---

## Dataset Summary

The dataset includes clinical and biochemical biomarkers.

| Variable        | Description                          |
|-----------------|--------------------------------------|
| Age             | Patient age                          |
| BMI             | Body mass index                      |
| Glucose         | Plasma glucose                       |
| Insulin         | Serum insulin                        |
| HOMA            | Insulin resistance index             |
| Leptin          | Hormone                              |
| Adiponectin     | Hormone                              |
| Resistin        | Hormone                              |
| MCP.1           | Chemokine                            |
| Classification  | 0 = Healthy, 1 = Cancer              |

---

## Preprocessing Steps

- Convert `Classification` to a factor  
- Remove missing values using `drop_na()`  
- Split dataset into training and testing sets using  
  `caret::createDataPartition()`  

---

## Model Training

A logistic regression model is fit using:

    model <- glm(
      Classification ~ Age + BMI + Glucose + Insulin + HOMA +
        Leptin + Adiponectin + Resistin + MCP.1,
      data = trainData,
      family = "binomial"
    )

---

## Purpose of This Project

This project was created to:

- Understand how logistic regression behaves on biomedical data  
- Practice interpreting coefficients and p-values  
- Build intuition around model transparency and explainability  

It is a **learning-focused statistical modeling exercise**, not a production or clinical prediction system.
