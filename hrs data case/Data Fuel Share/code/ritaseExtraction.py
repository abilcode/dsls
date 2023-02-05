import os 
import pandas as pd 
import numpy as np

def extract_ritase(data,month):
    cols_a = ['LOADER', 'EX42', 'Unnamed: 3', 'Unnamed: 4', 'Unnamed: 5',
       'Unnamed: 6', 'Unnamed: 7', 'Unnamed: 8', 'Unnamed: 9', 'Unnamed: 10',
       'Unnamed: 11', 'Unnamed: 12', 'Unnamed: 13', 'Unnamed: 14',
       'Unnamed: 15', 'Unnamed: 16', 'Unnamed: 17', 'Unnamed: 18',
       'Unnamed: 19', 'Unnamed: 20', 'Unnamed: 21', 'Unnamed: 22',
       'Unnamed: 23', 'Unnamed: 24','Unnamed: 25']
    
    cols_b = ['LOADER', 'EX44', 'Unnamed: 27',
       'Unnamed: 28', 'Unnamed: 29', 'Unnamed: 30', 'Unnamed: 31',
       'Unnamed: 32', 'Unnamed: 33', 'Unnamed: 34', 'Unnamed: 35',
       'Unnamed: 36', 'Unnamed: 37', 'Unnamed: 38', 'Unnamed: 39',
       'Unnamed: 40', 'Unnamed: 41', 'Unnamed: 42', 'Unnamed: 43',
       'Unnamed: 44', 'Unnamed: 45', 'Unnamed: 46', 'Unnamed: 47',
       'Unnamed: 48', 'Unnamed: 49']

    a,b = [0,0]
    df = [a,b]
    ex = ["EX42","EX44"]
    cols = [cols_a,cols_b]
    for i in range(2):
        df[i] = data[cols[i]]
        df[i]= df[i].rename(columns=df[i].iloc[0])
        df[i]= df[i].loc[1:,:]
        vars = pd.melt(df[i],id_vars=['JAM'],value_vars=df[i][1:])
        vars = vars.sort_values('JAM')
        vars['waktu'] = pd.to_datetime(vars.JAM) + vars.variable.astype('timedelta64[h]')
        df_fix = vars[['waktu','value']]
        df_fix.index = df_fix.waktu
        df_fix = df_fix.sort_index()
        df_fix['value'].to_csv(f"Data Fuel Share/data/extracted_ritase/{ex[i]}/ritase_{m}_{ex[i]}.csv")

def bind_ritase(data):
    pass

if __name__ == "__main__":

    print('=='*10,'Start','=='*10)
    month = ['Januari','Februari','Maret','April','Mei','Juni','Juli','Agustus','September','Oktober','November','Desember']
    for m in month :
        data = pd.read_excel("Data Fuel Share/data/RITASE EX-42-44 PERJAM 2022.xlsx",sheet_name=m,skiprows=[0])
        extract_ritase(data,m)
        print(f"Success extracting data ritase bulan {m}")
    print('=='*10,'Finished','=='*10)

