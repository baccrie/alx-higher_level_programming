#!/usr/bin/python3
import MySQLdb
from sys import argv

"""A module that performs magic"""


usern = argv[1]
passw = argv[2]
db = argv[3]

db = MySQLdb.connect(host='localhost', user=usern, passwd=passw, db=db, port=3306)
conn = db.cursor()
conn.execute("""SELECT * FROM states ORDER BY id ASC""")
result = conn.fetchall()
for x in result:
    print(x)
