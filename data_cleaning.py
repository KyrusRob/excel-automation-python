import pandas as pd

# Read data from Excel
df = pd.read_excel('output.xlsx')

# Basic cleaning: Fill missing values
df.fillna({'Score': 0}, inplace=True)

# Remove duplicates
df.drop_duplicates(inplace=True)

# Save cleaned data
df.to_excel('cleaned_data.xlsx', index=False)

print("Data cleaned and saved to 'cleaned_data.xlsx'")
