## Description
# This script performs basic data manipulation, filtering, and normalization on gene expression data.
# It also generates visualizations such as heatmaps and box plots.

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Load the saved CSV file
data_path = "GSE285299_expression_data.csv"
data = pd.read_csv(data_path)

# Display basic information about the data
print("Dataset Preview:")
print(data.head())
print("\nData Summary:")
print(data.info())
print("\nStatistical Description:")
print(data.describe())

# Ensure only numeric columns are processed (assuming the first column is gene IDs)
numeric_data = data.iloc[:, 1:].apply(pd.to_numeric, errors="coerce")
data.iloc[:, 1:] = numeric_data

# Drop rows with missing values (if any)
data = data.dropna()

# Filter genes with average expression > 1
filtered_data = data[data.iloc[:, 1:].mean(axis=1) > 1]

# Save the filtered data
filtered_data.to_csv("Filtered_GSE285299_expression_data.csv", index=False)
print("Filtered data saved as: Filtered_GSE285299_expression_data.csv")

# Normalization using log2 transformation
normalized_data = filtered_data.copy()
normalized_data.iloc[:, 1:] = np.log2(normalized_data.iloc[:, 1:] + 1)  # Add 1 to avoid log(0)

# Save the normalized data
normalized_data.to_csv("Normalized_GSE285299_expression_data.csv", index=False)
print("Normalized data saved as: Normalized_GSE285299_expression_data.csv")

# Visualization - Heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(normalized_data.iloc[:, 1:], cmap="viridis", cbar=True)
plt.title("Gene Expression Heatmap")
plt.xlabel("Samples")
plt.ylabel("Genes")
plt.tight_layout()
plt.savefig("Heatmap_GSE285299.png")
plt.show()

# Visualization - Box Plot
plt.figure(figsize=(12, 6))
sns.boxplot(data=normalized_data.iloc[:, 1:])
plt.title("Box Plot of Gene Expression Across Samples")
plt.xlabel("Samples")
plt.ylabel("Expression (log2 normalized)")
plt.xticks(rotation=90)
plt.tight_layout()
plt.savefig("BoxPlot_GSE285299.png")
plt.show()
