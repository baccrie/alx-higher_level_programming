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

    conn = MySQLdb.connect(host=hst, user=username, passwd=password, db=database, port=pt)
    cur = conn.cursor()
    cur.execute("""SELECT * FROM states ORDER BY id ASC""")
    res = cur.fetchall()
    for ststes in res:
        print(res)
    cur.close()
    conn.close()
