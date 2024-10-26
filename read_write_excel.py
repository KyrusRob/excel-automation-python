import pandas as pd

# Create a DataFrame with employee data
data = {
    'Employee': ['Alice', 'Bob', 'Charlie', 'Alice', 'David', 'Charlie', 'Eve'],
    'Department': ['Sales', 'HR', 'IT', 'Sales', 'HR', 'IT', 'Sales'],
    'Score': [85, 70, 95, 90, None, 95, 88]
}
df = pd.DataFrame(data)

# Write the DataFrame to Excel
df.to_excel('employee_performance.xlsx', index=False)

# Read the Excel file back
read_df = pd.read_excel('employee_performance.xlsx', engine='openpyxl')
print(read_df)

