#!/usr/bin/python3
"""A script that lists all states from hbtn_0e_0_usa DB"""


import MySQLdb
import sys


if (len(sys.argv) > 1):
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
else:
    pass

if __name__ == '__main__':
    db = MySQLdb.connect(
            host = "localhost",
            port = "3306",
            user = mysql_username,
            passwd = mysql_password,
            db = database_name
            )
    cursor = db.cursor()
    cursor.execute("SELECT states from hbtn_0e_0_usa ORDER BY id ASC")
    result = cursor.fetchall()
    for i in result:
        print(i)
    cursor.close()
    db.close()
