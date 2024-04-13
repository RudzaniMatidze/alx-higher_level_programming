#!/usr/bin/python3
"""A module that lists all states from mySQL database"""
import sys
import MySQLdb

if __name__ == "__main__":

    # Connects to the MySQL server
    db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3])

    # Creates a cursor object using cursor() method
    cursor = db.cursor()

    # Executes the SQL query to fetch all states
    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    # Fetches all the rows from the query result
    rows = cursor.fetchall()

    # Prints the results
    for row in rows:
        print(row)

    # Closes the database connection
    db.close()
