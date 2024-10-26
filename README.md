# Excel Automation with Python

This project demonstrates a complete end-to-end data flow using Python to automate Excel tasks. It includes reading/writing data, data cleaning, and generating a final report with charts. The dataset tracks employee performance, making the process consistent across all scripts.

## Project Overview
1. **Step 1 (`read_write_excel.py`)**: Creates the initial employee performance dataset.
2. **Step 2 (`data_cleaning.py`)**: Cleans and transforms the dataset.
3. **Step 3 (`generate_report.py`)**: Generates a report with department-wise average performance scores and charts.

## Project Structure
excel-automation-python/

- read_write_excel.py                # Creates initial data
- data_cleaning.py                   # Cleans the data
- generate_report.py                 # Generates a report with charts
- employee_performance.xlsx          # Initial data file
- cleaned_employee_performance.xlsx  # Cleaned data file
- employee_performance_report.xlsx   # Final report with charts
- README.md                          # Project documentation

## Requirements
- Python 3.x
- Libraries:
  - Pandas
  - OpenPyXL
  - XlsxWriter

To install the required libraries, run:
pip install pandas openpyxl xlsxwriter
