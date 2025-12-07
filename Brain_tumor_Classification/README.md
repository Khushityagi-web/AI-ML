# Brain Tumor Classification (CNN · Practice Project)

This project is a practice implementation of an end-to-end deep learning workflow for classifying brain tumor MRI images using Convolutional Neural Networks (CNNs).  
It was created during my early deep learning learning phase to understand the basics of image preprocessing, CNN model building, training, and evaluation.

The dataset used is from Kaggle:  
**Brain Tumor Classification (MRI)** by Sartaj Bhuvaji.

---

## 📌 Project Overview

This practice project includes:

- Dataset download using Kaggle CLI  
- Zip extraction and dataset inspection  
- Image loading & visualization  
- Image preprocessing  
  - resizing  
  - normalization  
- Train/test split  
- Handling class imbalance checks  
- Multiple CNN model iterations:
  - Baseline CNN
  - CNN + Dropout (to reduce overfitting)
  - CNN + Data Augmentation
  - CNN + Adjusted Dropout & lighter augmentation  
- Model training and validation  
- Evaluation using accuracy, confusion matrix, and classification report  
- Saving trained models (`.h5` format)

The goal was to understand *how CNNs behave in image classification tasks* rather than build a production model.

---

## 📁 File Structure

Brain_tumor_Classification/
│
├── script

---

## 🧠 Dataset Classes

The MRI dataset contains four categories:

- **glioma_tumor**  
- **meningioma_tumor**  
- **pituitary_tumor**  
- **no_tumor**

Images appear in both:
Training/
Testing/

---

## 🖼️ Preprocessing Steps

- Loaded images using OpenCV  
- Resized all images to **128 × 128**  
- Normalized pixel values (0–1)  
- Label-encoded class names  
- Split into training and testing sets (80/20)  
- Saved processed data into `preprocessed_data.pkl`

---

## 🤖 CNN Model Development

Multiple CNN architectures were tested:

### **1️⃣ Baseline CNN**
- Conv2D → MaxPool layers  
- Dense layer → Softmax output  
- 10 epochs training  

### **2️⃣ CNN with Dropout**
Added dropout after convolution and dense layers to reduce overfitting.

### **3️⃣ CNN + Data Augmentation**
Applied:
- rotations  
- shifts  
- shear  
- zoom  
- flips  

Trained for more epochs for better generalization.

### **4️⃣ CNN with Adjusted Dropout**
Reduced dropout levels and used lighter augmentation for stable training.

Each version was trained, evaluated, and saved separately.

Models saved as:

brain_tumor_cnn_model.h5
brain_tumor_cnn_improved_model.h5
brain_tumor_cnn_adjusted_model.h5


---

## 📈 Evaluation Metrics

After training each model, evaluation was performed using:

### ✔ Test accuracy  
Printed after model evaluation.

### ✔ Confusion matrix  
Plotted using seaborn to visualize misclassification patterns.

### ✔ Classification report  
Includes:
- precision  
- recall  
- f1-score  
for all four tumor classes.

### ✔ Prediction decoding  
Converted predicted indices back to original tumor labels.

---

## 🛠️ Requirements

Install required packages:

```bash
pip install kaggle opencv-python numpy tensorflow matplotlib seaborn scikit-learn
