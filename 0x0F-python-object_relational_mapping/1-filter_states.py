#!/usr/bin/python3
"""Module that lists all the states from the MySQL server"""
import sys
import MySQLdb

def filter_states(username, password, database):
    #connect to MySQL server
    db = MySQL.connect(
            host="Localhost",
            port=3306,
            user=username,
            passwd=password,
            db=database
            )

    cursor = db.cursor()
    
    #Execute SQL query to retrieve states starting with 'N'
    cursor.execute("SELECT * FROM sates WHERE name LIKE 'N%' ORDER BY id ASC")
    
    #Fetch all the rows
    rows = cursor.fetchall()

    #print the results
    for row in rows:
        print(row)

    #Close the database connection
    db.close()
