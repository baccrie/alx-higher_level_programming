#!/usr/bin/python3

"""
A magical Module
"""

from sys import argv
import MySQLdb


username = argv[0]
password = argv[1]
database = argv[2]

if __name__ == '__main__':
    conn = MySQLdb.connect(host='localhost', user=username, passwd=password, db=database, port=3306)
    cur = conn.cursor()
    cur.execute("""SELECT * FROM states ORDER BY id ASC""")
    cur.close()
    conn.close()
