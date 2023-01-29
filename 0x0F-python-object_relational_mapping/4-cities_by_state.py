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
    search = argv[4]

    conn = MySQLdb.connect(host=hst, user=username, passwd=password,
                           db=database, port=pt)
    cur = conn.cursor()
    cur.execute("""SELECT city.id, city.name,
                state.name FROM states as state INNER JOIN cities as city ON cities.id=
                states.id ORDER BY cities.id ASC""")
    res = cur.fetchall()
    for states in res:
        print(states)
    cur.close()
    conn.close()
