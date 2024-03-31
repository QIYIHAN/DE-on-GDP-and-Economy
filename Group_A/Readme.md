## 2013-2019_Counties_Data处理流程

所有数据的来源为2013-2019_Counties_Data.xlsx，请勿修改此文件中任何数据。

excel_to_csv.py为excel文件转csv文件脚本，需要的时候运行即可。

### 步骤一

​	运行fill_missing_step1.py，对2013-2019_Counties_Data.xlsx中D-O列的缺失值进行线性插值法补充。

​	得到文件fill_missing_step1.xlsx。

### 步骤二

​	运行updated_step2.py,对fill_missing_step1.xlsx中的特定两列进行两两相除得到新增列存入excel中。

​	得到文件updated_step2.xlsx。

### 步骤三

​	运行clean_columns_step3.py，对updated_step2.xlsx中指定列（两两相除的列）进行去除，并重命名特定列	名。

​	得到clean_columns_step3.xlsx。

### 步骤四

  通过相关系数矩阵来分析每两个变量之间的相关性，删除相关系数接近1的变量
  重新获得corr_columns_step5.xlsx

### 步骤五

  对面板数据使用线性回归模型，分析系数不为0（Hypothesis test)的变量，筛选出重要变量，将他们考虑进乡村经济指数的一部分。

### 步骤六

  通过PCA(选择一个主成分）方法，将最终选出来的五个重要变量变为一个主成分，该主成分由五个变量线性组合而成，可以用作为乡村经济指标（REI)
  将最终指数存为rural_economic_index_step6.xlsx
  

### 项目所需库：

| **numpy**    | **1.26.4** |
| ------------ | ---------- |
| **openpyxl** | **3.1.2**  |
| **pandas**   | **2.2.1**  |
| **xlrd**     | **2.0.1**  |
| **xlwt**     | **1.3.0**  |
