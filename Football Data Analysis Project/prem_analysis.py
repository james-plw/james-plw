import pandas as pd
import numpy as np

#importing csv file and converting to numpy array
df = pd.read_csv('matches.csv', sep=',', header=None)
arr = df.to_numpy()

headers = arr[0]
arr = np.delete(arr, 0, axis=0) #removing headers row

prem_arr = np.delete(arr, [0,3,15,18,19,26], axis=1) #removing useless columns
col_names = np.delete(headers, [0,3,15,18,19,26])

df2 = pd.DataFrame(prem_arr)
df2.to_csv("prem_data.csv", index=True, header=False)