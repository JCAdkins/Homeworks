# Jordan Adkins
# PA_12

import sqlite3
import re

conn = sqlite3.connect('ABCCorp.db')
curr = conn.cursor()
curr.execute('DROP TABLE IF EXISTS Customer')

curr.execute('''CREATE TABLE Customer(Column names TEXT, customer_number INTEGER, customer_name TEXT, balance REAL,
            credit_limit REAL, rep_num INTEGER)''')

customers = [('Row 1', 148, "Al's Appliance and Sport", 7550.0, 7500.0, 20),
             ('Row 2', 282, 'Brookings Direct', 431.5, 7500.0, 35),
             ('Row 3', 462, 'Bargains Galore', 3412.0, 10000.0, 65),
             ('Row 4', 524, "Kline's", 12762.0, 15000.0, 35),
             ('Row 5', 725, "Deerfield's Four Seasons", 248.75, 5000.0, 35),  #this should have the value 5000.0 as 5,000.0
             ('Row 6', 842, 'All Season', 8221.0, 7500.0, 20)]    #this should have 8,221.0 and 7,500.0

curr.executemany('INSERT INTO Customer VALUES (?,?,?,?,?,?)', customers)

sql = '''UPDATE Customer SET credit_limit = 10000.0 WHERE customer_number = 282'''
curr.execute(sql)

digit = 0
curr.execute("SELECT * FROM Customer ORDER BY 'Column'")

# trying to iterate through all the rows in the database but it only iterates once
for row in curr:
    digit = digit + 1                                                   # |
    rows = str(row[0])                                                  # |
    rows = re.sub(" \d+", '', rows)                                     # | These lines just put together the string
    sql = "UPDATE Customer SET 'Column' = "                             # | for the sql command to be executed
    rows = "'" + str(rows) + ' ' + str(digit) + "'"                     # |
    sql = sql + rows + " WHERE 'Column' = '" + str(row[0]) + "'"        # |
    print(sql)
    curr.execute(sql)

sql = '''DELETE FROM Customer WHERE customer_name = "Deerfield's Four Seasons"'''
curr.execute(sql)



conn.commit()
conn.close()
