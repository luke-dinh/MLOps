import pandas as pd

df = pd.read_csv("dataset.csv")
df.groupby("tag").size().plot.bar()