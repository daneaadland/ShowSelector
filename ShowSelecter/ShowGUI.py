'''
Created on Dec 30, 2017

@author: daneaadland
'''

import tkinter as tk
import numpy as np
import pandas as pd
import openpyxl



root = tk.Tk()

schema = ['Name', 'Seasons', 'Episodes', 'Rating', 'Current?', 'Type', 'App']
seed_data = [['It\'s Always Sunny', 12, 10, 9, 'Yes', 'Comedy', 'Hulu'], ['The Office', 9, 23, 8, 'No', 'Comedy', 'Netflix']]

tab = pd.DataFrame(seed_data, columns=schema)

wb = openpyxl.load_workbook('ShowTable.xlsx')
sheet = wb.get_sheet_by_name('Sheet1')


print(wb)
print(type(wb))
print(sheet)

#print(tab)

    

