import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load Dataset
df = pd.read_csv(r"C:\Users\USER\Downloads\task1\mynta_page(1-99).csv")

# Display Dataset Information
print("First 5 Rows:")
print(df.head())

print("\nDataset Information:")
print(df.info())

print("\nDataset Shape:")
print(df.shape)

# Check Missing Values
print("\nMissing Values:")
print(df.isnull().sum())

# Check Duplicate Rows
print("\nDuplicate Rows:")
print(df.duplicated().sum())

# Remove Duplicates
df.drop_duplicates(inplace=True)

# Convert Price to Numeric
df['Price'] = pd.to_numeric(
    df['Price'].astype(str).str.extract('(\d+)')[0],
    errors='coerce'
)

# Convert Discount to Numeric
df['Discount'] = pd.to_numeric(
    df['Discount'].astype(str).str.extract('(\d+)')[0],
    errors='coerce'
)

# Remove Null Values if Any
df.dropna(inplace=True)

# Summary Statistics
print("\nSummary Statistics:")
print(df.describe())

# -----------------------------
# Visualization 1: Boxplot
# -----------------------------
plt.figure(figsize=(8,5))
sns.boxplot(x=df['Selling Price'])
plt.title("Boxplot of Selling Price")
plt.show()

# -----------------------------
# Visualization 2: Top 10 Brands
# -----------------------------
top_brands = df['Brand'].value_counts().head(10)

plt.figure(figsize=(10,5))
sns.barplot(
    x=top_brands.index,
    y=top_brands.values
)

plt.title("Top 10 Brands")
plt.xlabel("Brand")
plt.ylabel("Count")
plt.xticks(rotation=45)
plt.show()

# -----------------------------
# Visualization 3: Selling Price Distribution
# -----------------------------
plt.figure(figsize=(8,5))
sns.histplot(
    df['Selling Price'],
    bins=30,
    kde=True
)

plt.title("Selling Price Distribution")
plt.xlabel("Selling Price")
plt.ylabel("Frequency")
plt.show()

# -----------------------------
# Visualization 4: Discount Distribution
# -----------------------------
plt.figure(figsize=(8,5))
sns.histplot(df['Discount'],
             bins=20,
             color='green')

plt.title("Discount Distribution")
plt.show()
# -----------------------------
# Visualization 5: Correlation Heatmap
# -----------------------------
plt.figure(figsize=(6,4))

sns.heatmap(
    df[['Selling Price', 'Price', 'Discount']].corr(),
    annot=True,
    cmap='coolwarm'
)

plt.title("Correlation Heatmap")
plt.show()

# -----------------------------
# Top Expensive Brands
# -----------------------------
print("\nTop Expensive Brands:")

brand_price = df.groupby('Brand')['Selling Price'].mean()

print(
    brand_price.sort_values(
        ascending=False
    ).head(10)
)