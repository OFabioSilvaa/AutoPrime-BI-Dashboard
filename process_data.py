import pandas as pd

excel_file = '/home/ubuntu/upload/exportfromsqliteonline.com.xlsx'
csv_file = '/home/ubuntu/autprime_data.csv'

df = pd.read_excel(excel_file)
df.to_csv(csv_file, index=False)

print(f'Arquivo {excel_file} convertido para {csv_file} com sucesso.')

