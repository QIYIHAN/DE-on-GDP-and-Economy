# Step 5: linear regression model (Panel data)

import statsmodels.api as sm
import pandas as pd

# Specify the Excel file path
excel_file_path5 = './corr_columns_step4.xlsx'

# Read Excel file
panel_data = pd.read_excel(excel_file_path5)

# Define X and Y in the linear regression model
X = panel_data[['Geographical area(sq. km)',
                'Primary Industry Added Value (in ten thousand yuan)',
                'Secondary Industry Added Value (in ten thousand yuan)',
                'Welfare Facilities Level(units)',
                'Population density (people per square kilometer)',
                'Telecommunication coverage level (households per ten thousand people)',
                'Human capital level (people per 10,000 people)',
                'Agricultural development level (yuan per person)',
                'Financial development level (yuan per person)'
]]
y = panel_data['Gross regional product (ten thousand yuan)']

# Add an intercept term
X = sm.add_constant(X)

# Fit a linear regression model
model = sm.OLS(y,X)
results = model.fit()

# Print the output
print(results.summary())
