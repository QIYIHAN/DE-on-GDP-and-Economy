# 此文件为步骤一，作用为补全2013-2019_Counties_Data.xlsx中所有缺失值，利用了线性插值法

import pandas as pd

# 指定Excel文件路径
excel_file_path = './2013-2019_Counties_Data.xlsx'
# 指定需要进行插值的列名列表
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

# 读取Excel文件
df = pd.read_excel(excel_file_path)

# 遍历列名列表，对每个列进行处理
for column_name in columns_to_interpolate:
    # 检查列是否存在
    if column_name in df.columns:
        # 对指定列进行线性插值
        df[column_name] = df[column_name].interpolate(method='linear')

        # 将插值结果四舍五入并转换为整数
        df[column_name] = df[column_name].round().astype(int)

        # 输出该列已完成的信息
        print(f"Interpolation and rounding completed for column: {column_name}")
    else:
        print(f"Column '{column_name}' not found in the DataFrame.")

# 保存修改后的DataFrame到新的Excel文件，如果文件已存在，则自动覆盖
output_file_path = './fill_missing_step1.xlsx'
df.to_excel(output_file_path, index=False)
print(f"Completed. The output is saved to {output_file_path}")
