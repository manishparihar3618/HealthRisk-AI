import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

print(df.shape)
print(df.dtypes)
print(df.head())
print(df.tail())
print(df.columns.tolist())

print(df.isnull().sum())
print((df.isnull().sum() / len(df)) * 100)

print(df.duplicated().sum())

print(df.describe())

if len(df.select_dtypes(include="object").columns) > 0:
    print(df.describe(include="object"))

for col in df.columns:
    print(col, df[col].nunique())

numeric_df = df.select_dtypes(include=np.number)

if not numeric_df.empty:
    corr = numeric_df.corr()

    plt.figure(figsize=(10, 8))
    plt.imshow(corr, cmap="coolwarm")
    plt.colorbar()
    plt.xticks(range(len(corr.columns)), corr.columns, rotation=90)
    plt.yticks(range(len(corr.columns)), corr.columns)
    plt.tight_layout()
    plt.show()

numeric_df.hist(figsize=(15, 10), bins=20)
plt.tight_layout()
plt.show()

for col in numeric_df.columns:
    plt.figure(figsize=(6, 4))
    plt.boxplot(df[col].dropna())
    plt.title(col)
    plt.show()

for col in df.select_dtypes(include=["object", "category"]).columns:
    print(df[col].value_counts())

for col in numeric_df.columns:
    q1 = df[col].quantile(0.25)
    q3 = df[col].quantile(0.75)
    iqr = q3 - q1
    lower = q1 - 1.5 * iqr
   
