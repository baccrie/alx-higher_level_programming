#!/usr/bin/python3

"""
A magical Module
"""

from sys import argv
import MySQLdb


if __name__ == '__main__':
    username = argv[1]
    password = argv[2]
    database = argv[3]
    hst = 'localhost'
    pt = 3306
    search = argv[4]

    conn = MySQLdb.connect(host=hst, user=username, passwd=password,
                           db=database, port=pt)
    cur = conn.cursor()
    cur.execute("""SELECT * FROM states WHERE name
                =%s ORDER BY id ASC""", (search, ))
    res = cur.fetchall()
    for states in res:
        print(states)
    cur.close()
    conn.close()
