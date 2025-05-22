import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv('dataset.csv')

# Compute correlation matrix
corr = df.corr(numeric_only=True)

# Plot heatmap
sns.heatmap(corr, annot=True, cmap='plasma')
plt.title("Feature Correlation Heatmap")
plt.show()