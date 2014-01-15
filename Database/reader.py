__author__ = 'benqing.shen'

import sqlite3

# Assuming you already have the database
conn = sqlite3.connect('data.db')

c = conn.cursor()

c.execute('''SELECT * FROM stocks LIMIT 10''')

for record in c.fetchall():
    print record

# conn.commit()

conn.close()