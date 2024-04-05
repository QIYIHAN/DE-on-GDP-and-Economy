# Step 3: Remove the columns used as dividend and divisor in step two from the table, and rename specific column names
import pandas as pd
# Specific the Excel file path
excel_file_path = './updated_step2.xlsx'

# Define the list of column names to be deleted
columns_to_delete = ['Landline subscribers (households)',
                     "Residents' Savings Deposit Balance (in ten thousand yuan)",
                     'Year-End Financial Institutions Total Loan Balance (in ten thousand yuan)',
                     'Number of Students in Secondary Vocational Education Schools (people)',
                     'Registered Population (in ten thousands)']

# Define a dictionary of column names to be renamed {original column name: new column name}
columns_to_rename = {'Administrative area (sq. km)': 'Geographical area(sq. km)',
                     'Number of industrial enterprises above designated size (units)': 'Level of Industrial Scale(units)',
                     'Number of Hospital Beds in Medical Health Institutions(units)': 'Healthcare Level(beds)',
                     'Number of Various Social Welfare Adoption Institutions(units)': 'Welfare Facilities Level(units)'}

# Read Excel file
df = pd.read_excel(excel_file_path)

# Iterate through and rename specific columns
for old_name, new_name in columns_to_rename.items():
    if old_name in df.columns:
        df.rename(columns={old_name: new_name}, inplace=True)
        print(f"Renamed column: {old_name} to {new_name}")
    else:
        print(f"Column to rename not found: {old_name}")

# Iterate through and delete columns
for column in columns_to_delete:
    if column in df.columns:
        df.drop(columns=[column], inplace=True)
        print(f"Deleted column: {column}")
    else:
        print(f"Column not found: {column}")

# Save the modified DataFrame to a new Excel file
output_file_path = './clean_columns_step3.xlsx'
df.to_excel(output_file_path, index=False)
print(f"Completed. The modified file is saved to {output_file_path}")
