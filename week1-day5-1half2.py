import pandas as pd
import numpy as np

# Load Clean Dataset

df = pd.read_csv("clean_data.csv")

print(df.head())

print("Dataset Loaded Successfully!")

# Summary Statistics

statistics = df[["age", "salary"]].agg(["mean", "median", "min", "max", "std"])

print("\nSummary Statistics:")
print(statistics)

# Department-wise Analysis

department_analysis = df.groupby("department").agg(
    employee_count=("employee_id","count",),
    average_salary=("salary", "mean"),
    average_age=("age", "mean")
)

print("\nDepartment Analysis:")
print(department_analysis)

# City-wise Analysis

city_analysis = df.groupby("city").agg(
    employee_count=("employee_id","count"),
    average_salary=("salary", "mean")

)

print("\nCity Analysis:")
print(city_analysis)

# Correlation Analysis

correlation = df[["age","salary"]].corr()

print("\nCorrelation Analysis:")
print(correlation)

# Business Questions

# Question 1: Which department has the highest average salary?
print("\nQuestion 1: Highest Salary Department")
print(
    df.groupby("department")["salary"].mean().idxmax()
    )

# Question 2: Which city has the most employees?
print("\nQuestion 2: City with Most Employees")
print(
    df["city"].value_counts().idxmax()
)

# Question 3: What is the overall average salary?
print("\nQuestion 3: Overall Average Salary")
print(
    df["salary"].mean()
)

# Department Budget Table

budget_data = {"department": ["It", "Hr", "Sales", "Finance"],
               "budget": [500000, 300000, 450000, 400000]}

budget_df = pd.DataFrame(budget_data)

print("\nDepartment Budget:")
print(budget_df)

# Merge Employee Data with Budget Data

merged_df = pd.merge(
    df,
    budget_df,
    on="department",
    how="left"
)

print("\nMerged Data:")
print(merged_df.head())


# Bonus: Pivot Table

pivot_table = pd.pivot_table(
    df,
    index="department",
    columns="city",
    values="salary",
    aggfunc="mean"
)

print("\nPivot Table:")
print(pivot_table)

# Save Final Dataset

merged_df.to_csv("final_employee_data.csv", index=False)

print("\nFinal Dataset Saved Successfully!")