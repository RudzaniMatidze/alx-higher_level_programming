#!/usr/bin/python3
""" a script that lists all states from the MySQL server"""

if __name__== '__main__':

    import MySQLdb
    import sys

    db = MySQLdb.connect(host='localhost', port=3306,
            user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])

    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY states.id ASC;")
    row = cur.fetchall()
    for row in rows:
        print(row)
