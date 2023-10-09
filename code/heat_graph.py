import numpy as np
import seaborn as sns
import pandas as pd
from matplotlib import pyplot as plt
# Load your CSV file into a DataFrame
df = pd.read_csv(r"C:\Users\newio\Downloads\Project\data_daily_clean.csv")
# Select the columns you want to include in the correlation analysis
selected_columns = df[['PM2.5', 'PM10', 'NOx', 'O3', 'CO', 'HR', 'NO', 'NO2', 'TMP']]
# Calculate the correlation matrix
corr = selected_columns.corr()
# Create a heatmap
plt.figure(figsize=(11, 8))
sns.heatmap(corr, cmap="pink", annot=True)
plt.show()
