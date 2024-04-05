# Step 4: Correlation analysis

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Specify the Excel file path
excel_file_path = './clean_columns_step3.xlsx'

# Read Excel file
df = pd.read_excel(excel_file_path)
# print(df)
# Remove the first three Columns (Year/County/Gross regional product)
X_variables = df.columns[3:]

# Calculate the correlation coefficient matrix among variables
correlation_matrix = df[X_variables].corr()

# Create a heatmap of correlation coefficients
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, fmt=".2f", cmap="coolwarm", center=0)
plt.title('Correlation Heatmap between Variables')
plt.show()

# Analysis: The range of the correlation coefficient is [-1, 1]. The closer this value is to -1 or 1, the stronger the correlation between two variables.
# Some variables have high correlarions:
# Level of industrial scale & secondary industry added value (0.86)
# Resident savings level & Financial development level (0.79)
# Healthcare level & Tertiary industry Empolyee (0.76)
# Tertiary Industry Employees & Level of industrial scale (0.61)
# Tertiary Industry Employees & Secondary industry added value (0.60)

# Based on the results of heatmap, remove variables that have high correlation with each other.
X_vars_updated = [var for var in X_variables if var not in [
    'Level of Industrial Scale(units)',
    'Resident savings level (yuan per person)',
    'Healthcare Level(beds)',
    'Tertiary Industry Employees (people)'
]]

# Recompute the correlation coefficient matrix using the updated list of variables.
corr_matrix_updated = df[X_vars_updated].corr()

# Establish new heatmap with updated X_variables
plt.figure(figsize=(10, 8))
sns.heatmap(corr_matrix_updated, annot=True, fmt=".2f", cmap="coolwarm", center=0)
plt.title('Updated Correlation Heatmap')
plt.show()
#  Define the list with high correlation
columns_to_delete2 = ['Level of Industrial Scale(units)',
                      'Resident savings level (yuan per person)',
                      'Healthcare Level(beds)',
                      'Tertiary Industry Employees (people)']

# Iterate through and delete columns
for column in columns_to_delete2:
    if column in df.columns:
        df.drop(columns=[column], inplace=True)
        print(f"Deleted column: {column}")
    else:
        print(f"Column not found: {column}")

# Save the modified DataFrame to a new Excel file
output_file_path = './corr_columns_step4.xlsx'
df.to_excel(output_file_path, index=False)
print(f"Completed. The modified file is saved to {output_file_path}")
