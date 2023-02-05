import os
import pandas as pd
import numpy as np

if __name__ == "__main__":
    print('Start!')
    dir_ = 'Data Fuel Share/data/extracted_ritase'
    filename_ = 'EX42'
    for dirpath, dirname, filename in os.walk(dir_+'/'+filename_):
        print(f"There are {len(dirname)} directories and {len(filename)} file in '{dirpath}'.")
    a,b,c,d,e,f,g,h,i,j,k,l = np.zeros(12)
    arr_con = [a,b,c,d,e,f,g,h,i,j,k,l]
    entries = os.listdir(f"{dir_}/{filename_}")
    n = len(entries)
    entries.sort()

    for i in range(n):
        arr_con[i] = pd.read_csv(f"{dir_}/{filename_}/{entries[i]}")
    append_data = pd.concat(arr_con,axis=0)
    append_data.waktu = pd.to_datetime(append_data.waktu)
    append_data.index = append_data.waktu
    append_data = append_data.sort_index()
    append_data['value'].to_csv(f"{dir_}/append_{filename_}.csv")
       
        
