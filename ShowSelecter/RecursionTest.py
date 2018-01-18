'''
Created on Jan 1, 2018

@author: daneaadland
'''

def test(x):
    if x < 1:
        print('All done!')
        return x
    else:
        print(x)
        test(x-1)
        
        
test(996)


import numpy
           
import pandas as pd
           
data = pd.DataFrame({'food': ['bacon', 'pulled pork', 'bacon', 'Pastrami','corned beef', 'Bacon', 'pastrami', 'honey ham','nova lox'],
                 'ounces': [4, 3, 12, 6, 7.5, 8, 3, 5, 6]})

data2 = pd.DataFrame({'names': ['Dane', 'Elizabeth', 'Minnie'], 'gender': ['Male', 'Female', 'Kittymale']})

data2['names']