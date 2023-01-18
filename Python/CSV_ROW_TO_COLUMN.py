import os
import pandas as pd
import numpy as np
from collections import OrderedDict, defaultdict
import csv

file_csv = input("Enter the file path:")

while(file_csv.endswith('.csv') is not True):
        print('Please enter .csv file')
        file_csv = input("Enter the file path: ")
while(os.path.exists(file_csv) is not True):
        print('File not exists.')
        file_csv = input("Please enter valid file path: ")

raw_data = pd.read_csv(file_csv, encoding='latin-1', sep=';', keep_default_na=False)

dict = raw_data.to_dict('split')
list_columns = pd.Series(dict['columns'])
list_data = pd.Series(dict['data'])

f_dict = {}
for count in list_columns.index:
        unique_list = []
        for d in list_data:
             item = str(d[count]).strip()
             if item != '' and  len(item) != 0 and item not in unique_list:
                    unique_list.append(item)

        f_dict[list_columns[count]]= tuple(unique_list)

result_file = input('Enter file name for result file: ')
result = pd.DataFrame.from_dict(f_dict, orient='index')
result.to_csv(result_file, header=False,  sep=';', encoding='latin-1')

