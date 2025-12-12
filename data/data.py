import os
import pandas as pd


xlsx_folder = 'data/xlsx'
csv_folder = 'data/csv'

os.makedirs(csv_folder, exist_ok=True)

for filename in os.listdir(xlsx_folder):
    if filename.endswith('.xlsx'):
        xlsx_path = os.path.join(xlsx_folder, filename)
        df = pd.read_excel(xlsx_path)
        csv_filename = os.path.splitext(filename)[0] + '.csv'
        csv_filename = csv_filename.replace('_import', '', 1)
        csv_path = os.path.join(csv_folder, csv_filename)
        df.to_csv(csv_path, index=False)