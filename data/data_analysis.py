import pandas as pd

# Data Distribution
df = pd.read_csv("dataset.csv")
df.groupby("tag").size().plot.bar()

# Check NaN value
print(df.isnull().sum().any())

