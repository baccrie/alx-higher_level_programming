#!/usr/bin/python3
"""A module that connects to a db and lists all states"""
import MySQLdb
from sys import argv

if name == '__main__':
    usern = argv[1]
    passw = argv[2]
    db = argv[3]

    db = MySQLdb.connect(user=usern, passwd=passw, db=db, port=3306)
    conn = db.cursor()
    conn.execute("""SELECT * FROM states ORDER BY id ASC""")
    result = conn.fetchall()
    for x in result:
        print(x)
