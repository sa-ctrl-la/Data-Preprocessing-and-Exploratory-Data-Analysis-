import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("mynta_page(1-99).csv")
print(df.head())
print(df.info())
print(df.shape)
df.isnull().sum()
df['size'].fillna(df['size'].mode()[0], inplace=True)
df['price'].fillna(df['price'].median(), inplace=True)
df.drop_duplicates(inplace=True)
sns.boxplot(x=df['price'])
print(df.describe())
print(df['color'].value_counts())
df['price'].hist(bins=30)
sns.countplot(x='color', data=df)
sns.boxplot(x='brand', y='price', data=df)
sns.heatmap(df.corr(), annot=True, cmap="coolwarm")