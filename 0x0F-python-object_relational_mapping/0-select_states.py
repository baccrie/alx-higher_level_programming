#!/usr/bin/python3
"""Lists all states from the database hbtn_0e_0_usa"""
import MySQLdb
from sys import argv


usern = argv[1]
passw = argv[2]
db = argv[3]

db = MySQLdb.connect(host='localhost', user=usern, passwd=passw, db=db, port=3306)
conn = db.cursor()
conn.execute("""SELECT * FROM states ORDER BY id ASC""")
result = conn.fetchall()
for x in result:
    print(x)
