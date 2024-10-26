import pandas as pd
import xlsxwriter

# Create a DataFrame
data = {'Department': ['Sales', 'HR', 'IT'], 'Revenue': [20000, 15000, 30000]}
df = pd.DataFrame(data)

# Create an Excel writer object
with pd.ExcelWriter('report.xlsx', engine='xlsxwriter') as writer:
    df.to_excel(writer, sheet_name='Summary', index=False)

    # Access the workbook and worksheet
    workbook = writer.book
    worksheet = writer.sheets['Summary']

    # Add a chart
    chart = workbook.add_chart({'type': 'column'})
    chart.add_series({
        'categories': ['Summary', 1, 0, 3, 0],
        'values':     ['Summary', 1, 1, 3, 1],
        'name':       'Revenue'
    })
    worksheet.insert_chart('E2', chart)

print("Report generated in 'report.xlsx'")
