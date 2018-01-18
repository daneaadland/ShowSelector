'''
Created on Jan 12, 2018

@author: daneaadland
'''

import sqlite3

cursor = db.cursor()
cursor.execute('''DROP TABLE users''')
db.commit()