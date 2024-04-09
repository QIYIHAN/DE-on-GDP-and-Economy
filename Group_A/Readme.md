## Processing Steps for 2013-2019_Counties_Data

All data is sourced from 2013-2019_Counties_Data.xlsx. Do not modify any data within this file.

The excel_to_csv.py script is used for converting Excel files to CSV format. Run this script when necessary.

### Step 1

​	Run fill_missing_step1.py to perform linear interpolation on missing values in columns D-O of 2013-2019_Counties_Data.xlsx.

  Output: fill_missing_step1.xlsx.

### Step 2

​	Run updated_step2.py to divide specific columns pairwise from fill_missing_step1.xlsx and store the results in a new Excel 
  file.
  
  Output: updated_step2.xlsx.

### Step 3

​	Run clean_columns_step3.py to remove specified columns (resulting from pairwise division) from updated_step2.xlsx and 
  rename specific columns.

  Output: clean_columns_step3.xlsx

### Step 4

  Analyze the correlation coefficient matrix to identify highly correlated variable pairs and remove variables with 
  coefficients close to 1.

  Obtain corr_columns_step5.xlsx after removing highly correlated variables.

### Step 5

  Apply linear regression models with panel data and analyze variables with non-zero coefficients (Hypothesis test) to 
  identify significant variables for later calculation of Rural Economic Index (REI).

### Step 6

  Utilize Principal Component Analysis (PCA) to combine the final selected five important variables into a single principal 
  component (P1) representing the Rural Economic Index (REI). This principal component is a linear combination of the five 
  variables.

  Save the final index as rural_economic_index_step6.xlsx.
  

### Required libraries for the project include:

| **numpy**    | **1.26.4** |
| ------------ | ---------- |
| **openpyxl** | **3.1.2**  |
| **pandas**   | **2.2.1**  |
| **xlrd**     | **2.0.1**  |
| **xlwt**     | **1.3.0**  |
