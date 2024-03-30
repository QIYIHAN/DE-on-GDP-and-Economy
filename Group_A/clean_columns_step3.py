# 此文件为步骤三，作用为将步骤二中用作被除数列和除数列的列从表中删除，并重命名特定列名

import pandas as pd

# 指定Excel文件路径
excel_file_path = './updated_step2.xlsx'

# 定义需要删除的列名列表
columns_to_delete = ['Landline subscribers (households)',
                     "Residents' Savings Deposit Balance (in ten thousand yuan)",
                     'Year-End Financial Institutions Total Loan Balance (in ten thousand yuan)',
                     'Number of Students in Secondary Vocational Education Schools (people)',
                     'Registered Population (in ten thousands)']

# 定义需要重命名的列名字典 {原列名: 新列名}
columns_to_rename = {'Administrative area (sq. km)': 'Geographical area (sq. km)',
                     'Number of industrial enterprises above designated size (units)': 'Level of Industrial Scale（units)',
                     'Number of Hospital Beds in Medical Health Institutions(units)': 'Healthcare Level(beds)',
                     'Number of Various Social Welfare Adoption Institutions(units)': 'Welfare Facilities Level（units)'}

# 读取Excel文件
df = pd.read_excel(excel_file_path)

# 遍历并重命名特定列
for old_name, new_name in columns_to_rename.items():
    if old_name in df.columns:
        df.rename(columns={old_name: new_name}, inplace=True)
        print(f"Renamed column: {old_name} to {new_name}")
    else:
        print(f"Column to rename not found: {old_name}")

# 遍历并删除列
for column in columns_to_delete:
    if column in df.columns:
        df.drop(columns=[column], inplace=True)
        print(f"Deleted column: {column}")
    else:
        print(f"Column not found: {column}")

# 保存修改后的DataFrame到新的Excel文件
output_file_path = './clean_columns_step3.xlsx'
df.to_excel(output_file_path, index=False)
print(f"Completed. The modified file is saved to {output_file_path}")
