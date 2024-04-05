# Step 1: Fill in missing values in the 2013-2019_Counties_Data.xlxs file with linear interpolation method.
import pandas as pd
# Specify the Excel file path
excel_file_path = './2013-2019_Counties_Data.xlsx'

# Specify the list of column names for interpolation
columns_to_interpolate = ['Gross regional product (ten thousand yuan)', 'Administrative area (sq. km)',
                          'Landline subscribers (households)', 'Primary Industry Added Value (in ten thousand yuan)',
                          'Secondary Industry Added Value (in ten thousand yuan)',
                          "Residents' Savings Deposit Balance (in ten thousand yuan)",
                          'Year-End Financial Institutions Total Loan Balance (in ten thousand yuan)',
                          'Number of industrial enterprises above designated size (units)',
                          'Number of Hospital Beds in Medical Health Institutions(units)',
                          'Number of Various Social Welfare Adoption Institutions(units)',
                          'Tertiary Industry Employees (people)',
                          'Number of Students in Secondary Vocational Education Schools (people)']

# Read Excel file
df = pd.read_excel(excel_file_path)

# Iterate through the list of column names and process each column
for column_name in columns_to_interpolate:

    # Check if the column exists
    if column_name in df.columns:

        # Perform linear interpolation on the specified column
        df[column_name] = df[column_name].interpolate(method='linear')

        # Round the interpolation results and convert them to integers
        df[column_name] = df[column_name].round().astype(int)

        # Output the completed column information
        print(f"Interpolation and rounding completed for column: {column_name}")
    else:
        print(f"Column '{column_name}' not found in the DataFrame.")

# Save the modified DataFrame to a new Excel file, automatically overwrite if the file already exists
output_file_path = './fill_missing_step1.xlsx'
df.to_excel(output_file_path, index=False)
print(f"Completed. The output is saved to {output_file_path}")