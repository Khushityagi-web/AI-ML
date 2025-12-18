# Brain Tumor Classification (CNN Practice Project)

This project is a practice implementation of an end-to-end deep learning workflow for classifying brain tumor MRI images using Convolutional Neural Networks (CNNs).

It was created during my early deep learning phase to understand the basics of image preprocessing, CNN model building, training, and evaluation.

The dataset used is from Kaggle:  
**Brain Tumor Classification (MRI)** by Sartaj Bhuvaji.

---

## Project Overview

This practice project includes:

- Dataset download using Kaggle CLI  
- ZIP extraction and dataset inspection  
- Image loading and visualization  
- Image preprocessing:
  - Resizing  
  - Normalization  
- Train/test split  
- Class imbalance checks  
- Multiple CNN model iterations:
  - Baseline CNN  
  - CNN with Dropout (to reduce overfitting)  
  - CNN with Data Augmentation  
  - CNN with adjusted Dropout and lighter augmentation  
- Model training and validation  
- Evaluation using accuracy, confusion matrix, and classification report  
- Saving trained models (`.h5` format)  

The goal of this project is to understand how CNNs behave in image classification tasks rather than to build a production-ready model.

---

## File Structure

    Brain_tumor_Classification/
    │── script.py
    │── README.md

---

## Dataset Classes

The MRI dataset contains four categories:

- `glioma_tumor`  
- `meningioma_tumor`  
- `pituitary_tumor`  
- `no_tumor`  

Images are organized into:

- `Training/`  
- `Testing/`  

---

## Preprocessing Steps

- Loaded images using OpenCV  
- Resized all images to **128 × 128**  
- Normalized pixel values to the range **0–1**  
- Label-encoded class names  
- Split data into training and testing sets (80/20)  
- Saved processed data to `preprocessed_data.pkl`  

---

## CNN Model Development

Multiple CNN architectures were tested.

### 1. Baseline CNN
- Convolutional (`Conv2D`) and max-pooling layers  
- Dense layer with softmax output  
- Trained for 10 epochs  

---

### 2. CNN with Dropout
- Added dropout after convolutional and dense layers  
- Reduced overfitting  

---

### 3. CNN with Data Augmentation
Applied:
- Rotations  
- Shifts  
- Shear  
- Zoom  
- Flips  

Trained for additional epochs to improve generalization.

---

### 4. CNN with Adjusted Dropout
- Reduced dropout levels  
- Used lighter augmentation for more stable training  

Each model version was trained, evaluated, and saved separately.

### Saved Models

- `brain_tumor_cnn_model.h5`  
- `brain_tumor_cnn_improved_model.h5`  
- `brain_tumor_cnn_adjusted_model.h5`  

---

## Evaluation Metrics

After training each model, evaluation was performed using:

### Test Accuracy
- Printed after model evaluation  

### Confusion Matrix
- Plotted using seaborn to visualize misclassification patterns  

### Classification Report
Includes:
- Precision  
- Recall  
- F1-score  

for all four tumor classes.

### Prediction Decoding
- Converted predicted class indices back to original tumor labels  

---

## Requirements

Install the required packages:

    pip install kaggle opencv-python numpy tensorflow matplotlib seaborn scikit-learn

