#!/usr/bin/python3
"""A module that connects to a db and lists all state
starting with letter N"""
import MySQLdb
from sys import argv

if __name__ == '__main__':
    usern = argv[1]
    passw = argv[2]
    db = argv[3]
    hs = 'localhost'
    pt = 3306

    db = MySQLdb.connect(host=hs, user=usern, passwd=passw, db=db, port=pt)
    con = db.cursor()
    con.execute("""SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC""")
    result = con.fetchall()
    for x in result:
        if x[1][0] != 'N':
            pass
        else:
            print(x)

    con.close()
    db.close()
