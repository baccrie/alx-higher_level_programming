#!/usr/bin/python3

"""
A magical module
"""


from sys import argv
import MySQLdb


if __name__ == '__main__':
    username = argv[1]
    password = argv[2]
    database = argv[3]
    hst = 'localhost'
    pt = 3306

    conn = MySQLdb.connect(host=hst, user=username, passwd=password,
                           db=database, port=pt)
    cur = conn.cursor()
    cur.execute("""SELECT c.id, c.name, s.name FROM cities as c
                      INNER JOIN states as s
                      ON c.state_id = s.id
                      ORDER BY c.id ASC;""")
    res = cur.fetchall()
    for states in res:
        print(states)
    cur.close()
    conn.close()
