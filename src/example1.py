import pandas as pd
import numpy as np

df = pd.read_csv("data/cereal.csv")

print(df)
print(df.info())
print(df.describe())