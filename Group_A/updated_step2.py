# Step2: Performing division operations on some specific two columns and inserting the resulting new column into the Excel file
import pandas as pd
# Specify the Excel file path
excel_file_path = './fill_missing_step1.xlsx'

# Define the column pairs to operate on and their resulting column names
# Format: (dividend column name, divisor column name, result column name)
columns_operations = [
    ('Registered Population (in ten thousands)', 'Administrative area (sq. km)',
     'Population density (people per square kilometer)'),
    ('Landline subscribers (households)', 'Registered Population (in ten thousands)',
     'Telecommunication coverage level (households per ten thousand people)'),
    (
    'Number of Students in Secondary Vocational Education Schools (people)', 'Registered Population (in ten thousands)',
    'Human capital level (people per 10,000 people)'),
    ('Primary Industry Added Value (in ten thousand yuan)', 'Registered Population (in ten thousands)',
     'Agricultural development level (yuan per person)'),
    ("Residents' Savings Deposit Balance (in ten thousand yuan)", 'Registered Population (in ten thousands)',
     'Resident savings level (yuan per person)'),
    ('Year-End Financial Institutions Total Loan Balance (in ten thousand yuan)',
     'Registered Population (in ten thousands)', 'Financial development level (yuan per person)')
    # 可以根据需要继续添加更多的列对
]

# specific columns
specific_column = 'Population density (people per square kilometer)'

# Read Excel file
df = pd.read_excel(excel_file_path)

# Iterate through each column pair for operation
for column_to_divide, column_divisor, new_column_name in columns_operations:

    # Ensure both columns exist
    if column_to_divide in df.columns and column_divisor in df.columns:

        # Perform division operation when the divisor is not zero
        df[new_column_name] = df[column_to_divide].div(df[column_divisor].replace(0, pd.NA))

        # If it's a specific column, multiply its value by 10000
        if new_column_name == specific_column:
            df[new_column_name] = df[new_column_name] * 10000

        # Round the results and convert them to integers
        df[new_column_name] = df[new_column_name].round().astype(int)
        # Output the information
        print(f"Interpolation and rounding completed for column: {new_column_name}")
    else:
        print(f"One or both columns '{column_to_divide}' and '{column_divisor}' do not exist in the DataFrame.")

# Save the modified DataFrame to a new Excel file.
output_file_path = './updated_step2.xlsx'
df.to_excel(output_file_path, index=False)
print(f"Completed. The output is saved to {output_file_path}")