# Step 6: Choose important variables and create new index as “Rural Economic Index”
# Use PCA to create the Index
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from step5 import panel_data

# Accirding to the results from linear regression, we thought below variables have strong influence on Gross regional product (95%):
# Primary Industry Added Value
# Secondary Industry Added Value
# Population desity
# Agricultural development level
# Financial development level
# We will use these variables to create "REI = Rural Economic Index"

data = panel_data[['Primary Industry Added Value (in ten thousand yuan)',
                   'Secondary Industry Added Value (in ten thousand yuan)',
                   'Population density (people per square kilometer)',
                   'Agricultural development level (yuan per person)',
                   'Financial development level (yuan per person)'
                   ]]

pca = PCA(n_components=1)  # Select one principal component

# Standardize the selected variables
scaler = StandardScaler()
scaled_data = scaler.fit_transform(data)

# Fit a PCA(Principal Component Analysis) model with the standarized data
pca.fit(scaled_data)

# Obtain the eigenvectors and eigenvalues.
eigenvectors = pca.components_
eigenvalues = pca.explained_variance_

# Generate "Rural Economic Index"
Rural_Economic_Index = pca.transform(data) / 100000

# Create new DataFrame (including REI)
result_df = panel_data[['Year', 'County']].copy()
result_df['Rural Economic Index (REI)'] = Rural_Economic_Index[:, 0]

# Output into Excel file
output_file_path = './rural_economic_index_step6.xlsx'
result_df.to_excel(output_file_path, index=False)
print(f"Completed. The modified file is saved to {output_file_path}")
