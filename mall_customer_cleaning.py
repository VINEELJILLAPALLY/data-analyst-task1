# mall_customer_cleaning.py
import pandas as pd

# 1. Load Dataset
df = pd.read_csv('Mall_Customers.csv')

# 2. Inspect Data
print("Initial shape:", df.shape)
print(df.head())

# 3. Check for missing values
print("\nMissing values before cleaning:\n", df.isnull().sum())

# Handle missing values (none expected in this dataset, but just in case)
df.fillna({
    'CustomerID': df['CustomerID'].mode()[0],
    'Gender': 'Not Specified',
    'Age': df['Age'].median(),
    'Annual Income (k$)': df['Annual Income (k$)'].mean(),
    'Spending Score (1-100)': df['Spending Score (1-100)'].mean()
}, inplace=True)

# 4. Remove duplicate rows
duplicates = df.duplicated().sum()
df.drop_duplicates(inplace=True)
print(f"\nRemoved {duplicates} duplicate rows.")

# 5. Standardize text (Gender column)
df['Gender'] = df['Gender'].str.lower().str.strip()

# 6. Rename columns for uniformity
df.columns = [
    'customer_id',
    'gender',
    'age',
    'annual_income_k',
    'spending_score'
]

# 7. Check and fix data types
df = df.convert_dtypes()

# 8. Final check
print("\nAfter cleaning:\n", df.info())
print("\nNulls after cleaning:\n", df.isnull().sum())

# 9. Save cleaned dataset
df.to_csv('Mall_Customers_Cleaned.csv', index=False)
print("\nCleaned dataset saved as 'Mall_Customers_Cleaned.csv'")
