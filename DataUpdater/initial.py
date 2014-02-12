__author__ = 'benqing.shen'

import sqlite3

# If this is your first time use.
conn = sqlite3.connect('pricedata.db')

c = conn.cursor()

c.execute('''
    CREATE TABLE stocks
    (
        symbol text,
        date text,
        open real,
        high real,
        low real,
        close real,
        volume real,
        price real,
        PRIMARY KEY (symbol, date)
    )
''')

conn.close()