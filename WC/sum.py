import pandas as pd

# 讀取 CSV 檔案
df = pd.read_csv('re.csv')

# 顯示前幾行資料以確認讀取成功
print(df.head())

# 提取不重複的 country 值
unique_countries = df['country'].drop_duplicates().reset_index(drop=True)
print("Unique countries:")
print(unique_countries)

# 提取不重複的 type 值
unique_types = df['type'].drop_duplicates().reset_index(drop=True)
print("Unique types:")
print(unique_types)

# 提取不重複的 grade 值
unique_grades = df['grade'].drop_duplicates().reset_index(drop=True)
print("Unique grades:")
print(unique_grades)

# 提取不重複的 type2 值
unique_type2s = df['type2'].drop_duplicates().reset_index(drop=True)
print("Unique type2s:")
print(unique_type2s)

# 提取不重複的 type2 值
unique_administration = df['administration'].drop_duplicates().reset_index(drop=True)
print("Unique administration:")
print(unique_administration)

# 儲存每個唯一值列表至不同的 CSV 檔案
unique_countries.to_csv('unique_countries.csv', index=False)
unique_types.to_csv('unique_types.csv', index=False)
unique_grades.to_csv('unique_grades.csv', index=False)
unique_type2s.to_csv('unique_type2s.csv', index=False)
unique_administration.to_csv('unique_administration.csv', index=False)
