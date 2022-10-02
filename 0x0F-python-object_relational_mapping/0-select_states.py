#!/usr/bin/python3
"""A script that lists all states from hbtn_0e_0_usa DB"""

if __name__ == '__main__':
    import MySQLdb
    import sys

    try:
        """mysql_username = sys.argv[1]
        mysql_password = sys.argv[2]
        database_name = sys.argv[3]

        db = MySQLdb.connect(
                host="localhost",
                port="3306",
                user=mysql_username,
                passwd=mysql_password,
                db=database_name
                )"""

        db = MySQLdb.connect(host='localhost', port=3306, user=argv[1], passwd=argv[2], db=argv[3])
    except Exception:
        print('Failed to connect to the database')
        exit(0)

    cursor = db.cursor()
    cursor.execute("SELECT * FROM states ORDER BY id ASC;")
    result = cursor.fetchall()
    for i in result:
        print(i)
    cursor.close()
    db.close()
