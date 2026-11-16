import pandas as pd
import numpy as np

# Create Employee Dataset
import pandas as pd
import numpy as np

df = pd.DataFrame({
    "employee_id": range(1, 101),
    "name": [f"Employee_{i}" for i in range(1, 101)],
    "age": np.random.randint(22, 60, 100),
    "salary": np.random.randint(20000, 100000, 100),
    "department": np.random.choice(["IT", "HR", "Sales", "Finance"], 100),
    "city": np.random.choice(["Chennai", "Mumbai", "Delhi", "Bangalore"], 100)
                              
})

print(df.head())

print("Dataset Created Succesfully!")


# Add Missing Values

df.loc[2, "age"] = np.nan
df.loc[5, "salary"] = np.nan
df.loc[8, "department"] = np.nan
df.loc[10, "city"] = np.nan

print(df.isnull().sum())

# Add Duplicate Records

df = pd.concat([df, df.iloc[:5]], ignore_index=True)
print("Before Removing Duplicates:")
print(len(df))

# Remove Duplicates

df = df.drop_duplicates()

print("After Removing Duplicates:")
print(len(df))

print("Duplicates Removed Successfully!")

# Standardise Text

text_columns = ["name", "department", "city"]

for column in text_columns:
    df[column] = df[column].str.strip().str.title()

print("\nStandardised Data:")
print(df.head(10))

# Handle Missing Values

# Age - Median
df["age"] = df["age"].fillna(df["salary"].median())

# Salary - Median
df["salary"] = df["salary"].fillna(df["salary"].median())

# Department - Mode
df["department"] = df["department"].fillna(df["department"].mode()[0])

# City - mode
df["city"] = df["city"].fillna(df["city"].mode()[0])

# Check Missing Values

print("\nMissing Values After Cleaning:")
print(df.isnull().sum())

# Outlier Detection Using IQR

numeric_columns = ["age", "salary"]

for column in numeric_columns:
    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)

    IQR = Q3 - Q1

    lower_limit = Q1 - (1.5 * IQR)
    upper_limit = Q3 + (1.5 * IQR)

    outliers = df[
        (df[column] < lower_limit) |
        (df[column] > upper_limit)
    ]
    print("\nOutliers in", column)
    print(outliers[column])
    print("Total Outliers:", len(outliers)) 

    # Before and After Summery

    after_rows = len(df)

    after_missing = df.isnull().sum().sum()

    after_duplicates = df.duplicated().sum()

    summary = pd.DataFrame({
        "Metric": ["Rows", "Missing Values", "Duplicates"],

        "Before": [
            105,
            5,
            5
        ],

        "After": [
            after_rows,
            after_missing,
            after_duplicates

        ]
    })

    print("\nBefore and After Summary")
    print(summary)

# Save clean Data

df.to_csv("clean_data.csv",index=False)

print("Clean Data Saved Successfully!")

summary.to_csv("before_after_summary.csv", index=False)

print("Summary Saved Successfully!")
