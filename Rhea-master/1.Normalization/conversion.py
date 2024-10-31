import pandas as pd
file_path = 'zOTU-Table_V1V3_stool_Renamed_58_Taxonomy.xlsx'
df = pd.read_excel(file_path)

df.to_csv('zOTU-Table_V1V3_stool_Renamed_58_Taxonomy.tab', sep='\t', index=False)