import pandas as pd

# Create a DataFrame
data = {'Name': ['Alice', 'Bob', 'Charlie'], 'Score': [85, 90, 95]}
df = pd.DataFrame(data)

# Write DataFrame to Excel
df.to_excel('output.xlsx', index=False)

# Read the Excel file
read_df = pd.read_excel('output.xlsx')
print(read_df)
