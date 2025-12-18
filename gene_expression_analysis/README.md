# Gene Expression Preprocessing & Visualization (GSE285299)

This project demonstrates basic preprocessing, filtering, and visualization on gene expression data from the **GSE285299** dataset.

The focus of this project is to practice essential data-handling steps used in transcriptomics workflows, not to perform full-scale differential expression or biological interpretation.

---

## Project Overview

This repository is an early experiment where I first explored how to:

- Inspect raw gene expression matrices  
- Clean and filter the data  
- Apply simple log-normalization  
- Generate foundational QC plots (heatmap and boxplot)  

---

## Workflow Summary

### 1. Load & Inspect Data
- Preview dataset structure  
- Check data types and missing values  
- Generate summary statistics  

---

### 2. Cleaning
- Convert sample columns to numeric  
- Drop genes with missing values  

---

### 3. Filtering
- Retain genes with mean expression > 1  

This step is used as a simple thresholding exercise and is not biologically optimized.

---

### 4. Normalization
- Apply log2 transformation (`log2(x + 1)`)  
- Save normalized expression matrix  

---

### 5. Visualization
- Heatmap of log-normalized expression  
- Boxplot across samples  

Saved outputs:
- `Heatmap_GSE285299.png`  
- `BoxPlot_GSE285299.png`  

---

## Repository Structure

    gene_expression_analysis/
    │── script.py
    │── README.md

---

## Skills Demonstrated

- Handling raw gene expression datasets  
- Cleaning, numeric conversion, and filtering  
- Log2 normalization  
- Heatmap and boxplot generation using seaborn  
- Reproducible workflow structuring  
- Basic QC visualization concepts in transcriptomics  

---

## Limitations

This project is intentionally simple:

- No TPM / CPM / RPKM normalization  
- No PCA, clustering, or DEG analysis  
- Filtering threshold not biologically optimized  
- Visualizations intended for practice, not research-level interpretation  

It serves as an introductory preprocessing exercise rather than a full analysis.

---

## Future Improvements

- Add deeper QC (PCA, sample distance matrix)  
- Apply variance-stabilizing transformations  
- Perform differential expression analysis  
- Annotate genes using biomaRt or Ensembl APIs  


