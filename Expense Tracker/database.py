import sqlite3
conn=sqlite3.connect("ExpenseTracker.db")

print("opened database successfully!")
try:
    conn.execute("""CREATE TABLE IF NOT EXISTS Expense
    (username CHAR(10)  NOT NULL,
    item CHAR(20) NOT NULL,
    tag TEXT NOT NULL,
    type TEXT NOT NULL,
    amount INT ,
    edate CHAR(10)
    );""")
except:
    print()

print("Table created successfully")

conn.execute('''CREATE TABLE IF NOT EXISTS User
    (
    username CHAR(20) NOT NULL,
    passwrod CHAR(20) NOT NULL,
    budget INT NOT NULL
    );''')
print("Table created successfully")

try:
    conn.execute('''CREATE TABLE IF NOT EXISTS Budget
    (
    username CHAR(20) NOT NULL,
    item CHAR(20) NOT NULL,
    lim INT
    );''')

except:
    print()

print("Table created successfully")


li=[['suman','pizza','others','expense',200,'2020/11/03'],
['suman','movie','entertainment','expense',300,'2020/11/22'],
['suman','bill','utilities','expense',500,'2020/10/02'],
['suman','old age','pension','income',1000,'2020/11/25'],
['suman','diwali','gift income','income',500,'2020/10/02'],
['suman','salary','salary','income',10000,'2020/09/01'],
['suman','child edu','Education','expense',5000,'2020/09/01'],
['suman','bonus','bonus','income',2000,'2020/08/28'],
['suman','other','others','expense',1000,'2020/08/28']]

for i in li:
    conn.execute("""INSERT INTO Expense VALUES(?,?,?,?,?,?);""",i)
print("data entry successful!")
conn.commit()
print("now showing the data: ")

conn.execute("""INSERT INTO User VALUES('suman','123',10000)""")
conn.commit()

conn.execute("INSERT INTO Budget VALUES('suman','movie',1000)")
conn.commit()