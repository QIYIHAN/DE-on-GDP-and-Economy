# 此文件为步骤二，作用为进行特定两列的除法运算，将得到的新列插入excel中

import pandas as pd

# 指定Excel文件路径
excel_file_path = './fill_missing_step1.xlsx'

# 定义需要进行操作的列对及其结果列名称
# 格式：(被除数列名, 除数列名, 结果列名)
columns_operations = [
    ('Registered Population (in ten thousands)', 'Administrative area (sq. km)', 'Population density (people per square kilometer)'),
    ('Landline subscribers (households)', 'Registered Population (in ten thousands)', 'Telecommunication coverage level (households per ten thousand people)'),
    ('Number of Students in Secondary Vocational Education Schools (people)', 'Registered Population (in ten thousands)', 'Human capital level (people per 10,000 people)'),
    ('Primary Industry Added Value (in ten thousand yuan)', 'Registered Population (in ten thousands)', 'Agricultural development level (yuan per person)'),
    ("Residents' Savings Deposit Balance (in ten thousand yuan)", 'Registered Population (in ten thousands)', 'Resident savings level (yuan per person)'),
    ('Year-End Financial Institutions Total Loan Balance (in ten thousand yuan)', 'Registered Population (in ten thousands)', 'Financial development level (yuan per person)')
    # 可以根据需要继续添加更多的列对
]
# 特殊列
specific_column = 'Population density (people per square kilometer)'
# 读取Excel文件
df = pd.read_excel(excel_file_path)

# 遍历每组列进行操作
for column_to_divide, column_divisor, new_column_name in columns_operations:
    # 确保两列都存在
    if column_to_divide in df.columns and column_divisor in df.columns:
        # 执行除法操作，除数不为0的情况下
        df[new_column_name] = df[column_to_divide].div(df[column_divisor].replace(0, pd.NA))
        # 如果是特定的列，则将其值乘以 10000
        if new_column_name == specific_column:
            df[new_column_name] = df[new_column_name] * 10000
        # 将插值结果四舍五入并转换为整数
        df[new_column_name] = df[new_column_name].round().astype(int)
        # 输出该列已完成的信息
        print(f"Interpolation and rounding completed for column: {new_column_name}")
    else:
        print(f"One or both columns '{column_to_divide}' and '{column_divisor}' do not exist in the DataFrame.")

# 保存修改后的DataFrame到新的Excel文件
output_file_path = './updated_step2.xlsx'
df.to_excel(output_file_path, index=False)
print(f"Completed. The output is saved to {output_file_path}")
