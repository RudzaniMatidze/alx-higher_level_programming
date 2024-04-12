#!/usr/bin/python3
"""Module that lists all the states from the MySQL server"""
import sys
import MySQLdb


if __name__ = "__main__":
    #Get MySQL credentials from command-line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    #Connect to MySQL server
    db = MySQLdb.connect(user=username, passwd=password, db=database)
    c = db.cursor()

    #Execute the SQL query to retrieve all states sorted id
    c.execute("SELECT * FROM `states` ORDER BY `id`")

    #Print states starting with 'N'
    for state in c.fetchall():
        if state[1][0] == "N":
            print(state)

    #Close the database connectiion
    db.close()
