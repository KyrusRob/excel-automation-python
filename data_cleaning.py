import pandas as pd

# Read the employee performance data
df = pd.read_excel('employee_performance.xlsx', engine='openpyxl')

# Fill missing values in 'Score' with the average score using a more compatible approach
average_score = df['Score'].mean()
df.loc[:, 'Score'] = df['Score'].fillna(average_score)

# Remove duplicate entries
df = df.drop_duplicates()

# Save the cleaned data to a new file
df.to_excel('cleaned_employee_performance.xlsx', index=False)

print(f"Data cleaned and saved to 'cleaned_employee_performance.xlsx'")
