# Jordan Adkins
# PA_12

import sqlite3

conn = sqlite3.connect('ABCCorp.db')
curr = conn.cursor()
curr.execute('DROP TABLE IF EXISTS Customer')

curr.execute('''CREATE TABLE Customer(customer_number INTEGER PRIMARY KEY, customer_name TEXT, balance REAL,
            credit_limit REAL, rep_num INTEGER)''')

customers = [(148, "Al's Appliance and Sport", 7550.0, 7500.0, 20),
             (282, 'Brookings Direct', 431.5, 7500.0, 35),
             (462, 'Bargains Galore', 3412.0, 10000.0, 65),
             (524, "Kline's", 12762.0, 15000.0, 35),
             (725, "Deerfield's Four Seasons", 248.75, 5000.0, 35),  #this should have the value 5000.0 as 5,000.0
             (842, 'All Season', 8221.0, 7500.0, 20)]    #this should have 8,221.0 and 7,500.0

curr.executemany('INSERT INTO Customer VALUES (?,?,?,?,?)', customers)

sql = '''UPDATE Customer SET credit_limit = 10000.0 WHERE customer_number = 282'''
curr.execute(sql)

sql = '''DELETE FROM Customer WHERE customer_name = "Deerfield's Four Seasons"'''
curr.execute(sql)

sql = '''SELECT * FROM Customer WHERE credit_limit >= 10000.0 AND rep_num = 35 ORDER BY credit_limit DESC'''
curr.execute(sql)
currCursor = curr.fetchall()
digit = 0
for rows in range(currCursor.__len__()):
    print(str(currCursor[digit][1]) + ' - $' + str(currCursor[digit][3]))
    digit = digit + 1

sql = '''SELECT * FROM Customer WHERE balance > credit_limit '''
curr.execute(sql)
currCursor = curr.fetchall()
digit = 0
for rows in range(currCursor.__len__()):
    print(currCursor[digit])
    digit = digit + 1


conn.commit()
conn.close()
