# 此文件仅用作将excel转为csv文件，无其他作用
# 项目运行请从step1开始逐一运行

import pandas as pd

# 定义Excel文件的路径
excel_file_path = './xxxxxxx.xls'
# 定义输出CSV文件的路径
csv_file_path = './xxxxxxx.csv'

# 读取Excel文件
df = pd.read_excel(excel_file_path)

# 将DataFrame保存为CSV文件
df.to_csv(csv_file_path, index=False)
