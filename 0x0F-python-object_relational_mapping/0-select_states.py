#!/usr/bin/python3
"""
A module that c9nnects to db and performs magic
"""

import MySQLdb


db = MySQLdb.connect(
        user='root',
        read_default_file="~/.my.cnf",
        database='hbtn_0e_0_usa'
        )
cursor = db.cursor()
cursor.execute("""SELECT * FROM states ORDER BY id ASC""")
result = cursor.fetchall()
for x in result:
    print(x)
