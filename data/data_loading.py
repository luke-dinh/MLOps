import pandas as pd

# Load dataset
data_url = "https://raw.githubusercontent.com/GokuMohandas/Made-With-ML/main/datasets/projects.csv"
df_data = pd.read_csv(data_url)

# Load label
label_url = "https://raw.githubusercontent.com/GokuMohandas/Made-With-ML/main/datasets/tags.csv"
df_label = pd.read_csv(label_url)

# Create dataset
data_final = pd.merge(df_data, df_label, on="id")
data_final = data_final[data_final.tag.notnull()]
data_final.to_csv("data/dataset.csv")