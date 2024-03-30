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

### 项目所需库：

| **numpy**    | **1.26.4** |
| ------------ | ---------- |
| **openpyxl** | **3.1.2**  |
| **pandas**   | **2.2.1**  |
| **xlrd**     | **2.0.1**  |
| **xlwt**     | **1.3.0**  |