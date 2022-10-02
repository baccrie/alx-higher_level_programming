#!/usr/bin/python3
"""A script that lists all states from hbtn_0e_0_usa DB"""

if __name__ == '__main__':
    import MySQLdb
    import sys

    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    try:
        db = MySQLdb.connect(
                host="localhost",
                port="3306",
                user=mysql_username,
                passwd=mysql_password,
                db=database_name
                )
    except Exception:
        exit(0)

    cursor = db.cursor()
    cursor.execute("SELECT * FROM states ORDER BY id ASC;")
    result = cursor.fetchall()
    for i in result:
        print(i)
    cursor.close()
    db.close()
