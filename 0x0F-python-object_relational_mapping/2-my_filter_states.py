#!/usr/bin/python3
"""A module that connects to a db and lists all state
where name matches argv[4]"""
import MySQLdb
from sys import argv

if __name__ == '__main__':
    usern = argv[1]
    passw = argv[2]
    db = argv[3]
    hs = 'localhost'
    pt = 3306
    search = argv[4]

    db = MySQLdb.connect(host=hs, user=usern, passwd=passw, db=db, port=pt)
    con = db.cursor()
    cmd = """SELECT * FROM states ORDER BY id ASC"""
    con.execute(cmd)
    result = con.fetchall()
    for x in result:
        if x[1] != search:
            pass
        else:
            print(x)

    con.close()
    db.close()
