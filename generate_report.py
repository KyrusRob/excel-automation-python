import pandas as pd
import xlsxwriter

# Read the cleaned employee performance data
df = pd.read_excel('cleaned_employee_performance.xlsx', engine='openpyxl')

# Calculate average score by department
dept_avg = df.groupby('Department')['Score'].mean().reset_index()

# Create an Excel writer object for the report
with pd.ExcelWriter('employee_performance_report.xlsx', engine='xlsxwriter') as writer:
    # Write the cleaned data to a sheet
    df.to_excel(writer, sheet_name='Cleaned Data', index=False)

    # Write department-wise average scores to another sheet
    dept_avg.to_excel(writer, sheet_name='Department Averages', index=False)

    # Access the workbook and worksheet
    workbook = writer.book
    worksheet = writer.sheets['Department Averages']

    # Add a bar chart for average scores
    chart = workbook.add_chart({'type': 'column'})
    chart.add_series({
        'categories': ['Department Averages', 1, 0, len(dept_avg), 0],
        'values': ['Department Averages', 1, 1, len(dept_avg), 1],
        'name': 'Average Score'
    })
    chart.set_title({'name': 'Average Score by Department'})
    worksheet.insert_chart('D2', chart)

print("Report generated in 'employee_performance_report.xlsx'")
