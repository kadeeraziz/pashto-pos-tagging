#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import glob



path = r'.' # File paths
all_files = glob.glob(path + "/*.xlsx")

dictionary = []

for filename in all_files:
    df = pd.read_excel(filename, index_col=None, header=0)
    dictionary.append(df)

frame = pd.concat(dictionary, axis=0, ignore_index=True)



frame = frame.sort_values('tag')


#frame.isna().any()[lambda x: x]



# drop null values
frame.dropna()



# save dictionary to a file
frame.to_excel('dictionary.xlsx', index=False)



